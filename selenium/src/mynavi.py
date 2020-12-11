from pprint import pprint as pp
import os, time, re, csv, threading
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import process, scrap
from modules import conversion as cv
from modules.webdriver import Chrome


def get_corp_by_mynavi(indst_id, csv_path):
    """マルチプロセス内で処理"""
    url = 'https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/index'
    ch = Chrome()
    driver = ch.driver
    driver.get(url)

    # 初期選択解除
    driver.find_element_by_xpath('//*[@id="indGroup0"]/div/p/span[2]/a') # 業種解除
    driver.find_element_by_xpath('//*[@id="areaGroup0"]/div/p/span[2]/a') # エリア解除

    # 業種選択
    ch.click(xpath=f'//*[@id="indCategory{indst_id}"]') # 業種
    ch.click(xpath=f'//*[@id="indGroup{indst_id}"]/div/p/span[1]/a') # 全て選択
    ch.click(xpath='//*[@id="doSearchTypeIndustryArea2"]') # 検索
    time.sleep(2)
    # ページネーション取得
    tmp = re.split('[(/)]', driver.find_element_by_xpath('//*[@id="contentsleft"]/div[1]/div[2]/ul/li[2]/span').text)
    n_pages = int(tmp[2])
    print('総ページ数：', tmp[2])

    for i in range(n_pages):
        print('進捗：', i + 1)
        # 表示された会社数を取得
        el_list = driver.find_elements_by_class_name('boxSearchresultEach')
        time.sleep(8)

        # 会社情報を取得
        for i, _ in enumerate(el_list):
            corp_el = driver.find_element_by_xpath(f'//*[@id="corpNameLink[{i}]"]')
            corp = {
                'name': corp_el.text, # 会社名
                'link': corp_el.get_attribute('href') # 詳細ページURL
            }
            cv.add_row(csv_path, corp.values())

        # 次の100件へ
        try:
            ch.click(xpath='//*[@id="upperNextPage"]')
        except Exception as e:
            print(e)
            return
    ch.end()


def get_detailpage_link():
    """会社名と詳細ページURL取得"""
    # 業種選定
    indst_lst = [
        {'id': '0', 'name': 'maker'},
        {'id': '1', 'name': 'trading'},
        {'id': '2', 'name': 'retail'},
        {'id': '3', 'name': 'finance'},
        {'id': '4', 'name': 'service'},
        {'id': '5', 'name': 'software'},
        {'id': '6', 'name': 'ad'},
        {'id': '7', 'name': 'public'},
    ]

    # 企業情報を取得
    threads = []
    for indst in indst_lst:
        # industory info
        indst_id = indst['id']
        indst_name = indst['name']
        csv_path = f"_storage/mynavi/{indst_name}.csv"
        # start thread
        t = threading.Thread(
            target=get_corp_by_mynavi,
            args=(indst_id, csv_path))
        t.setDaemon(True)
        t.start()
        threads.append(t)
    process.wait_all_threads(threads)


def get_about_corp(corp):
    """企業の詳細データを取得
        return: {
            name: 企業名
            tel: 電話番号
            url: 企業HP
            email: メールアドレス
            page_link: マイナビURL,
            location: 本社所在地
        }
    """
    corp_name = corp[0]
    page_link = corp[1]
    sc = scrap.ScrapHTML(page_link)
    html = sc.html

    def get_val(item_name):
        """テキストをスクレイピング"""
        el = html.select(f"th:contains({item_name})", limit=1)
        if el:
            text = el[0].parent.td.text
            text = text.replace('　', ' ')
        else:
            text = ''
        return text
    def get_contact():
        el = html.select('#corpDescDtoListDescText110')
        if el:
            text = el[0].text
            text = text.replace('　', ' ')
        else:
            text = ''
        return text
    # 取得
    # url = get_val('URL')
    # url = re.findall('(?P<url>https?://[^\s]+)', url)
    return {
        'url': get_val('URL'),
        'name': corp_name,
        'tel': get_val('本社電話番号'),
        'email': get_val('E-mail'),
        'location': get_val('本社所在地'),
        'contact': get_contact(),
        'page_link': page_link,
    }


if __name__ == '__main__':
    # 1. 会社名と詳細ページURL取得
    # get_detailpage_link()

    # 2. 詳細ページからデータを取得・csv作成
    print('***** CSV出力を開始します。*****')
    print('\n読み込むCSVファイル名を指定してください。')
    filename = f"{input('>> ')}.csv" # ex)finance
    print('\n同時処理数を指定してください。')
    process_range = int(input('>> '))
    print('\n開始レコード番号を入力してください。')
    start_rec = int(input('>> ')) -1
    print('\n終了レコード番号を入力してください。')
    end_rec = int(input('>> ')) -1

    from_csv = f"./_storage/mynavi/{filename}"
    to_csv = f"./_storage/mynavi/@{filename}"

    # csvから企業一覧取得
    corp_lst = cv.csv_to_list(csv_path=from_csv)
    if end_rec:
        corp_lst = corp_lst[start_rec:end_rec]
    else:
        corp_lst = corp_lst[start_rec:]
    sp_corp_lst = process.split_list(corp_lst, process_range)

    # 5個ずつの二次元配列
    for sub_lst in sp_corp_lst:
        # 企業ごとにデータ取得(マルチプロセス)
        with Pool(process_range) as p:
            result_lst = p.map(get_about_corp, sub_lst)
            # csv出力
            for corp in result_lst:
                cv.add_row(
                    csv_path=to_csv,
                    val_list=corp.values()
                )


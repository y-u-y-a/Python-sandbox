from pprint import pprint as pp
import time, re, csv, threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import process, scrap
from modules import conversion as cv
from modules.webdriver import Chrome


def get_corp_by_mynavi(indst_id, csv_path):
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


def get_about_corp(corp_name, page_link):
    """企業の詳細データを取得
        return: 企業名、電話番号、メールアドレス、企業HP、マイナビURL
    """
    sc = scrap.ScrapHTML(page_link)
    html = sc.html

    def get_val(item_name) -> str:
        el = html.select(f"th:contains({item_name})", limit=1)
        if el:
            val = el[0].parent.td.text
        else:
            val = None
        return val
    # 取得
    return {
        'name': corp_name,
        'tel': get_val('本社電話番号'),
        'url': get_val('URL'),
        'email': get_val('E-mail'),
        'page_link': page_link
    }


if __name__ == '__main__':
    # # 1. 会社名と詳細ページURL取得
    # get_detailpage_link()
    # 2. 詳細ページからデータを取得・csv作成
    # TODO: csvからページリンクなどを二次元配列で取得
    result = get_about_corp(
        corp_name='XXX株式会社',
        page_link='https://job.mynavi.jp/21/pc/search/corp91256/outline.html'
    )
    pp(result)

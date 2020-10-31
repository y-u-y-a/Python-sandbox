import pprint
import os, time, math, threading, csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import conversion as cv
from modules import webdriver as wd
from modules import process


def write_to_sheet(book, sheet, row, corp) -> None:
    """シート書き込み"""
    try:
        sheet.cell(row=row, column=1, value=corp['name'])
        sheet.cell(row=row, column=2, value=corp['phone_number'])
        return
    except Exception:
        return

def get_phone_number(corp_name) -> str:
    """会社名から電話番号の更新"""

    ch = wd.Chrome()
    driver = ch.driver
    serach_word = f'{corp_name} 電話番号'
    # start
    driver.get('https://google.com/')
    serach_form = driver.find_element_by_name('q')
    serach_form.send_keys(serach_word)
    serach_form.submit()
    try:
        phone_number = driver.find_element_by_class_name('mw31Ze').text
    except Exception:
        phone_number = ''
    # end
    finally:
        driver.quit()
        return phone_number

# CSVへ書き込み
def add_phone_number(w, corp_name):
    phone_number = get_phone_number(corp_name)
    w.writerow([corp_name, phone_number])
    print(corp_name)
    return


if __name__ == '__main__':

    # # 1. csvデータの取得
    # cv.excel_to_csv(
    #     xlsx_path='_storage/kaden.xlsx',
    #     csv_path='./_storage/kaden.csv',
    #     sheet_name='Type', # シート名を指定
    #     usecols=[1], # 使用する列を指定
    #     index_col=0)
    def split_list(l, n):
        """
        リストをサブリストに分割する
        l: リスト
        n: サブリストの要素数
        """
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]

    # 2. 電話番号を追加したCSVに追記
    from_csv = '_storage/kaden.csv'
    to_csv = '_storage/new.csv'
    with open(from_csv, 'r') as fr, open(to_csv, 'a') as fw:
        r = csv.reader(fr)
        w = csv.writer(fw)
        # CSVをリストに変換して取得
        rows = [row[0] for row in r]
        sp_list = list(split_list(rows, 5))
        # 並列処理
        threads = []
        for i, sub_list in enumerate(sp_list):
            for j, corp_name in enumerate(sub_list):
                # corp_index = i*5 + j
                t = threading.Thread(
                    target=add_phone_number,
                    args=(w, corp_name))
                t.setDaemon(True)
                t.start()
                threads.append(t)
            process.wait_all_threads(threads)

    # 3. シート作成・書込み
    # book = cv.create_excel_book('./_storage/result.xlsx')
    # sheet = book.worksheets[0]
    # sheet.title = 'サンプルシート'
    # with open(to_csv, 'r') as f:
    #     r = csv.reader(f)
    #     corp = dict()
    #     for row in r:
    #         corp['name'] = row[0]
    #         corp['phone_number'] = row[1]

import pprint
import os, time, math, threading, csv, codecs
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import conversion as cv
from modules import webdriver as wd
from modules import process

def split_list(l, n):
    """指定した要素数の2次元配列に変換
    l: 元リスト
    n: サブリストの要素数
    """
    for idx in range(0, len(l), n):
        yield list(l[idx:idx + n])


def get_phone_number(corp_name) -> str:
    """会社名から電話番号を取得"""

    ch = wd.Chrome()
    serach_word = f'{corp_name} 電話番号'
    with ch.driver as driver:
        # driver = ch.driver
        driver.get('https://google.com/')
        serach_form = driver.find_element_by_name('q')
        serach_form.send_keys(serach_word)
        serach_form.submit()
        try:
            phone_number = driver.find_element_by_class_name('mw31Ze').text
        except Exception:
            phone_number = ''
        finally:
            # driver.quit()
            return phone_number


def write_to_sheet(book, sheet, row, corp) -> None:
    """シート書き込み"""
    try:
        sheet.cell(row=row, column=1, value=corp['name'])
        sheet.cell(row=row, column=2, value=corp['phone_number'])
        return
    except Exception:
        return


def update_corp_dict(corp):
    corp['phone_number'] = get_phone_number(corp['name'])
    return corp


if __name__ == '__main__':

    # # 1. csvデータの取得
    # cv.excel_to_csv(
    #     xlsx_path='_storage/kaden.xlsx',
    #     csv_path='./_storage/kaden.csv',
    #     sheet_name='Type', # シート名を指定
    #     usecols=[1], # 使用する列を指定
    #     index_col=0)

    # 2. 会社名のみのcsvから電話番号込みのcsvを作成
    from_csv = '_storage/kaden.csv'
    to_csv = '_storage/new.csv'
    keyname_list = ['name']

    corp_list = cv.csv_to_dicts(from_csv, keyname_list)
    sp_corp_list = split_list(corp_list, 5) # 分割
    for sub_list in sp_corp_list:
        # マルチプロセスで処理
        with Pool(5) as p:
            result_list = p.map(update_corp_dict, sub_list)
            pprint.pprint(result_list)
            # csv出力
            for corp in result_list:
                cv.add_row(to_csv, corp.values())


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

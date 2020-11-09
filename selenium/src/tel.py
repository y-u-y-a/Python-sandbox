import pprint
import os, time, math, threading, csv, codecs
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import conversion as cv
from modules import webdriver as wd
from modules import process


def get_phone_number(corp_name) -> str:
    """会社名から電話番号を取得"""

    ch = wd.Chrome()
    serach_word = f'{corp_name} 電話番号'
    with ch.driver as driver:
        driver.get('https://google.com/')
        serach_form = driver.find_element_by_name('q')
        serach_form.send_keys(serach_word)
        serach_form.submit()
        try:
            phone_number = driver.find_element_by_class_name('mw31Ze').text
        except Exception:
            phone_number = ''
        finally:
            return phone_number


def update_corp_dict(corp):
    corp_name = corp['name']
    corp['phone_number'] = get_phone_number(corp_name)
    return corp



if __name__ == '__main__':

    ######################
    # # 1. csvデータの取得
    ######################
    # cv.excel_to_csv(
    #     xlsx_path='_storage/kaden.xlsx',
    #     csv_path='./_storage/kaden.csv',
    #     sheet_name='Type', # シート名を指定
    #     usecols=[1], # 使用する列を指定
    #     index_col=0)


    ###########################################
    # 2. 会社名のみのcsvから電話番号込みのcsvを作成
    ###########################################
    # from_csv = '_storage/kaden/kaden.csv'
    # to_csv = '_storage/kaden/new.csv'
    # keyname_list = ['name']
    # process_range = 5

    # tmp = cv.csv_to_dicts(from_csv, keyname_list)
    # corp_list = tmp[600:] # csvの行番号+1と一致
    # sp_corp_list = process.split_list(corp_list, process_range) # 分割

    # for sub_list in sp_corp_list:
    #     # マルチプロセスで処理(5個ずつ)
    #     with Pool(process_range) as p:
    #         # 順に取得
    #         result_list = p.map(update_corp_dict, sub_list)
    #         # csv出力
    #         for corp in result_list:
    #             cv.add_row(to_csv, corp.values())


    #########################
    # 3. 新規シート作成・書込み
    #########################
    input_csv = '_storage/kaden/new.csv'
    xlsx_path = './_storage/type.xlsx'
    sheet_name = 'サンプルシート'
    label_lst = ['会社名', '電話番号']

    # シート作成
    book = cv.create_excel_book(xlsx_path)
    sheet = book.worksheets[0]
    sheet.title = sheet_name
    # csvを2次元配列に変換
    lst = cv.csv_to_list(input_csv)
    # 書き込み
    cv.write_to_sheet(sheet, lst, label_lst=label_lst)
    book.save(xlsx_path)

import os, time, math, threading, csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from modules import conversion as cv
from modules import webdriver as wd
from modules import process


def write_to_sheet(book, sheet, row, company) -> None:
    """シート書き込み"""
    try:
        sheet.cell(row=row, column=1, value=company['name'])
        sheet.cell(row=row, column=2, value=company['phone_number'])
        return
    except Exception:
        return

def get_phone_number(company_name) -> str:
    """会社名から電話番号の更新"""

    ch = wd.Chrome()
    driver = ch.driver
    serach_word = f'{company_name} 電話番号'
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


if __name__ == '__main__':

    # # 1. csvデータの取得
    # cv.excel_to_csv(
    #     xlsx_path='_storage/kaden.xlsx',
    #     csv_path='./_storage/kaden.csv',
    #     sheet_name='Type', # シート名を指定
    #     usecols=[1], # 使用する列を指定
    #     index_col=0)

    # 2. 電話番号を追加したCSVに追記
    from_csv = '_storage/kaden.csv'
    to_csv = '_storage/new.csv'
    with open(from_csv, 'r') as fr, open(to_csv, 'a') as fw:
        r = csv.reader(fr)
        w = csv.writer(fw)
        # CSVをリストに変換して取得
        for row in r:
            company_name = row[0]
            phone_number = get_phone_number(company_name)
            w.writerow([company_name, phone_number])
            print(company_name)

    # 3. シート作成・書込み
    # book = cv.create_excel_book('./_storage/result.xlsx')
    # sheet = book.worksheets[0]
    # sheet.title = 'サンプルシート'
    # with open(to_csv, 'r') as f:
    #     r = csv.reader(f)
    #     company = dict()
    #     for row in r:
    #         company['name'] = row[0]
    #         company['phone_number'] = row[1]

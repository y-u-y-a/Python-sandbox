import os, time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import openpyxl as exl

from libs import converter

DRIVER_PATH = os.environ['DRIVER_PATH']


def get_driver():
    """ driverを取得 """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--lang=ja') # configure language
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    return driver


def get_excel_file():
    converter.excel_to_csv(
        input_file_path='_files/company_list.xlsx',
        output_file_path='./_files/company_list.csv',
        sheet_name=1,
        usecols=[1, 3, 4, 5, 11],
        index_col=0
    )

def write_to_excel_file(book, sheet, output_path, company, row):
    """シート書き込み"""
    sheet.cell(row=row, column=1, value=company['name'])
    sheet.cell(row=row, column=2, value=company['url'])
    sheet.cell(row=row, column=3, value=company['charge'])
    sheet.cell(row=row, column=4, value=company['appointment'])
    sheet.cell(row=row, column=5, value=company['phone_number'])
    sheet.cell(row=row, column=6, value=company['phone_number_2'])
    book.save(output_path)
    return




def main():
    # [input]
    output_path: str = './_files/output.xlsx'
    sheet_name: str = 'wantedly_list'
    company_list: list = converter.csv_to_dicts(
        file_path='_files/company_list.csv',
        dict_keys=['name', 'url', 'charge', 'appointment', 'phone_number']
    )
    url: str = 'https://google.com/'
    input_form: str = 'q'
    driver = get_driver()
    # シート作成
    book = exl.Workbook()
    sheet = book.create_sheet(index=0, title=sheet_name)

    for i, company in enumerate(company_list):
        # 検索
        serach_word = f"{company['name']} 電話番号"
        driver.get(url)
        serach_form = driver.find_element_by_name(input_form)
        serach_form.send_keys(serach_word)
        serach_form.submit()
        try:
            if i == 0:
                company['phone_number_2'] = '取得電話番号'
            else:
                phone_number = driver.find_element_by_class_name('mw31Ze').text
                company['phone_number_2'] = phone_number
        except Exception:
            company['phone_number_2'] = ''
        time.sleep(1)
        # シート書込み
        write_to_excel_file(book, sheet, output_path, company, row=i+1)
        print(i)
    # end
    driver.quit()




if __name__ == '__main__':
    main()

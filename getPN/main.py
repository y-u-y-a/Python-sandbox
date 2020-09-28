import pprint
import os, time, math, threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import openpyxl as exl

from libs import converter as cvt
from libs import parallel

DRIVER_PATH = os.environ['DRIVER_PATH']

# 最初のみ
def get_excel_file():
    cvt.excel_to_csv(
        input_file_path='_files/company_list.xlsx',
        output_file_path='./_files/company_list.csv',
        sheet_name=1,
        usecols=[1, 3, 4, 5, 11],
        index_col=0)
    return


def get_driver():
    """ driverを取得 """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--lang=ja') # configure language
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    return driver

def write_to_sheet(book, sheet, row, dict) -> None:
    """シート書き込み"""
    try:
        sheet.cell(row=row, column=1, value=dict['name'])
        sheet.cell(row=row, column=2, value=dict['url'])
        sheet.cell(row=row, column=3, value=dict['charge'])
        sheet.cell(row=row, column=4, value=dict['appointment'])
        sheet.cell(row=row, column=5, value=dict['phone_number'])
        sheet.cell(row=row, column=6, value=dict['phone_number_2'])
    except Exception:
        return
    return


def update_company(company) -> dict:
    """電話番号の更新"""
    # start
    driver = get_driver()
    url = 'https://google.com/'
    name_of_el = 'q'
    # 検索
    serach_word = f"{company['name']} 電話番号"
    driver.get(url)
    serach_form = driver.find_element_by_name(name_of_el)
    serach_form.send_keys(serach_word)
    serach_form.submit()
    try:
        phone_number = driver.find_element_by_class_name('mw31Ze').text
        company['phone_number_2'] = phone_number
    except Exception:
        company['phone_number_2'] = ''
    time.sleep(1)
    # end
    driver.quit()
    return company


def main():
# 流れ #########################
# 1. シートを作成
# 2. csvデータをdictの配列に変換
# 3. 会社情報の更新・取得
# 4. ラベル追加
# 5. シート書込み
################################

    # 1. ブック・シート作成
    sheet_name: str = 'wantedly_list'
    output_path: str = './_files/output.xlsx'
    book = exl.Workbook()
    sheet = book.create_sheet(index=0, title=sheet_name)

    # 2. csvデータをdictの配列に変換
    input_file_path: str = '_files/test.csv'
    dict_keys: list = ['name', 'url', 'charge', 'appointment', 'phone_number']
    company_list: list = cvt.csv_to_dicts(
        file_path=input_file_path,
        dict_keys=dict_keys)

    # 3. 会社情報の更新・取得
    result = []
    def get_company(company, serial_index) -> None:
        """会社情報の更新と追加"""
        company = update_company(company)
        result.append(company)
        pprint.pprint(serial_index)
        return

    i = 0
    thread_num = 5
    loop_times = math.ceil(len(company_list)/thread_num)
    for _ in range(loop_times):
        threads = []
        for j in range(thread_num):
            serial_index = i*thread_num + j # 会社の通し番号として使用
            company = company_list[serial_index]
            t = threading.Thread(
                target=get_company,
                args=(company, serial_index))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        parallel.wait_all_threads(threads)
        i += 1


    # 4. ラベルの追加
    sheet_label = {
        'name': '会社名',
        'url': 'URL',
        'charge': '担当者',
        'appointment': '結果',
        'phone_number': '電話番号',
        'phone_number_2': '取得電話番号'
    }
    result.insert(0, sheet_label)
    # 5. シート書込み
    for i, company in enumerate(result):
        pprint.pprint(company)
        write_to_sheet(book, sheet, row=i+1, dict=company)
        book.save(output_path)


if __name__ == '__main__':
    main()

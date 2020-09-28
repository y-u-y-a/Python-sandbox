import pprint
import os, time, math, threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl as exl

from libs import converter as cvt
from libs import parallel

DRIVER_PATH = os.environ['DRIVER_PATH']

# # 最初のみ
# def get_csv_from_excel() -> None:
#     cvt.excel_to_csv(
#         input_file_path='_files/company_list.xlsx',
#         output_file_path='./_files/company_list.csv',
#         sheet_name=1,
#         usecols=[1, 3, 4, 5, 11],
#         index_col=0)
#     return


# csvから取得〜sheetに書き込み
def write_to_sheet(book, sheet, row, company) -> None:
    """シート書き込み"""
    try:
        sheet.cell(row=row, column=1, value=company['id'])
        sheet.cell(row=row, column=2, value=company['name'])
        sheet.cell(row=row, column=3, value=company['url'])
        sheet.cell(row=row, column=4, value=company['charge'])
        sheet.cell(row=row, column=5, value=company['appointment'])
        sheet.cell(row=row, column=6, value=company['phone_number'])
        sheet.cell(row=row, column=7, value=company['phone_number_2'])
        return
    except Exception:
        return


def get_phone_number(company_name) -> str:
    """電話番号の更新"""

    def get_driver():
        """driverを取得"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=ja') # configure language
        driver = webdriver.Chrome(DRIVER_PATH, options=options)
        return driver

    # [input]
    driver = get_driver()
    url = 'https://google.com/'
    name_of_el = 'q'
    serach_word = f"{company_name} 電話番号"
    # start
    driver.get(url)
    serach_form = driver.find_element_by_name(name_of_el)
    serach_form.send_keys(serach_word)
    serach_form.submit()
    try:
        phone_number = driver.find_element_by_class_name('mw31Ze').text
    except Exception:
        phone_number = ''
    finally:
        # end
        driver.quit()
        time.sleep(1)
        return phone_number


def main():
    # 1. ブック・シート作成
    book = exl.Workbook()
    sheet = book.worksheets[0]
    sheet.title = 'wantedly_list'
    output_path: str = './_files/output.xlsx'

    # 2. csvデータをdictの配列に変換
    input_file_path: str = '_files/company_list.csv'
    dict_keys: list = ['name', 'url', 'charge', 'appointment', 'phone_number']
    company_list: list = cvt.csv_to_dicts(
        file_path=input_file_path,
        dict_keys=dict_keys)

    # 3. 会社情報の更新・取得
    result = []
    def update_company(company, serial_index) -> None:
        """会社情報の更新と追加"""
        company['id'] = serial_index
        company['phone_number_2'] = get_phone_number(company['name'])
        result.append(company)
        print(serial_index)
        return

    # [並列処理]
    i = 0
    thread_range = 25 # 同時スレッドの数を指定
    loop_times = math.ceil(len(company_list)/thread_range)
    for _ in range(loop_times):
        threads = []
        for j in range(thread_range):
            serial_index = i*thread_range + j # listにおける会社の通し番号として使用
            company = company_list[serial_index]
            t = threading.Thread(
                target=update_company,
                args=(company, serial_index))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        parallel.wait_all_threads(threads)
        i += 1

    # 4. idで並び順を整理
    result: list = sorted(result, key=lambda x: x['id'])

    # 5. ラベルの追加
    sheet_label: dict = {
        'id': 'No.',
        'name': '会社名',
        'url': 'URL',
        'charge': '担当者',
        'appointment': '結果',
        'phone_number': '電話番号',
        'phone_number_2': '取得電話番号'
    }
    result.insert(0, sheet_label)
    # 6. シート書込み
    for i, company in enumerate(result):
        write_to_sheet(book, sheet, row=i+1, company=company)
        book.save(output_path)



if __name__ == '__main__':
    # get_csv_from_excel()
    main()

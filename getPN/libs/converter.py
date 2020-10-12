import csv, codecs, pprint

import chardet
import pandas as pd
import openpyxl as exl

SHIFT_JIS = 'shift_jis'
UTF_8 = 'utf-8'

############################
# エンコーディング関係
############################
def get_encoding(file_path):
    """ファイルのencodingを取得"""

    encoding = ''
    with codecs.open(file_path, mode='rb') as f:
        content = chardet.detect(f.read())
        encoding = content['encoding']
    return encoding


def convert_encoding(input_path, output_path, from_encoding=SHIFT_JIS, to_encoding=UTF_8):
    """encodingを変換してファイルへ書き込み"""

    input_file = codecs.open(input_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(output_path, mode='w', encoding=to_encoding)

    for row in input_file:
        output_file.write(row)

    input_file.close()
    output_file.close()


############################
# 拡張子関係
############################
def tsv_to_csv(tsv_path, csv_path, from_encoding=SHIFT_JIS, to_encoding=UTF_8):
    """encodingを指定してTSVファイルをCSVファイルに変換"""

    input_file = codecs.open(tsv_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(csv_path, mode='w', encoding=to_encoding)

    # delimiter is tab
    data = csv.reader(input_file, delimiter='\t')
    target_file = csv.writer(output_file, delimiter=',')

    for row in data:
        target_file.writerow(row)

    input_file.close()
    output_file.close()


def csv_to_dicts(csv_path, dict_keys):
    """csvファイルをlistに変換"""
    result_list = []
    with open(csv_path, mode='r', encoding=UTF_8) as f:
        get_list = csv.DictReader(f, dict_keys)
        for row in get_list:
            result_list.append(dict(row))
    return result_list


############################
# エクセル関係
############################
def excel_to_csv(xlsx_path, csv_path, sheet_name, usecols, index_col=0) -> None:
    """
    excelのsheetを指定してCSVに変換
    xlsx_path: 読み込むExcelファイルのパス
    csv_path: 書き出すCSVのファイル名
    sheet_name: CSVに変換するExcelのシート名
    use_cols: 0始まりで列を指定
    """
    # read sheet
    df = pd.read_excel(
        xlsx_path,
        sheet_name=sheet_name,
        index_col=index_col,
        usecols=usecols
    )
    df.to_csv(csv_path)
    return

def create_excel_book(book_path):
    """excelブックを作成"""
    book = exl.Workbook()
    book.save(book_path)
    return book

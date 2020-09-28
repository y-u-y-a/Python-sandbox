import csv, codecs, pprint

import chardet
import pandas as pd
import openpyxl as exl


def get_encoding(file_path):
    """ファイルのencodingを取得"""

    encoding = ''
    with codecs.open(file_path, mode='rb') as f:
        content = chardet.detect(f.read())
        encoding = content['encoding']
    return encoding


def convert_encoding(input_path, output_path, from_encoding='shift_jis', to_encoding='utf-8'):
    """encodingを変換してファイルへ書き込み"""

    input_file = codecs.open(input_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(output_path, mode='w', encoding=to_encoding)

    for row in input_file:
        output_file.write(row)

    input_file.close()
    output_file.close()


# use codecs
def tsv_to_csv(input_path, output_path, from_encoding='shift_jis', to_encoding='utf-8'):
    """encodingを指定してTSVファイルをCSVファイルに変換"""

    input_file = codecs.open(input_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(output_path, mode='w', encoding=to_encoding)

    # delimiter is tab
    data = csv.reader(input_file, delimiter='\t')
    target_file = csv.writer(output_file, delimiter=',')

    for row in data:
        target_file.writerow(row)

    input_file.close()
    output_file.close()


# use pandas
def excel_to_csv(input_file_path, output_file_path, sheet_name, usecols, index_col=0):
    """エクセルのシートを指定してCSVに変換"""
    # read sheet
    df = pd.read_excel(input_file_path, sheet_name=sheet_name, index_col=index_col, usecols=usecols)
    df.to_csv(output_file_path)
    return


# use codecs
def csv_to_dicts(file_path, dict_keys):
    """csvファイルをlistに変換"""
    result_list = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        get_list = csv.DictReader(f, dict_keys)
        for row in get_list:
            result_list.append(dict(row))
    return result_list

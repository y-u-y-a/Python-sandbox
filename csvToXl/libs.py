import csv, codecs
import chardet

# import numpy as np
# import pandas as pd
# import openpyxl as excel

def get_encoding(file_path):
    """get file encoding"""

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
    # テスト用
    # for index, row in enumerate(input_file):
    #     output_file.write(row)
    #     if index == 10:
    #         break



def convert_tsv(input_path, output_path, from_encoding='shift_jis', to_encoding='utf-8'):
    """encodingを指定してTSVファイルをCSVファイルに変換する"""

    input_file = codecs.open(input_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(output_path, mode='w', encoding=to_encoding)

    # 区切りがタブであることを指定
    data = csv.reader(input_file, delimiter='\t')
    target_file = csv.writer(output_file)

    for row in data:
        target_file.writerow(row)

    input_file.close()
    output_file.close()

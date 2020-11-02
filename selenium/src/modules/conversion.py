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
    """ファイルのencodingを取得
    file_path: エンコーディングを知りたいファイルのパスを指定
    """
    encoding = ''
    with codecs.open(file_path, mode='rb') as f:
        content = chardet.detect(f.read())
        encoding = content['encoding']
    return encoding


def convert_encoding(input_path, output_path, from_encoding=SHIFT_JIS, to_encoding=UTF_8) -> None:
    """encodingを変換してファイルへ書き込み
    input_path: エンコードしたいファイルのパスを指定
    output_path: エンコード後に書き出すファイルパスを指定
    """
    input_file = codecs.open(input_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(output_path, mode='w', encoding=to_encoding)

    for row in input_file:
        output_file.write(row)

    input_file.close()
    output_file.close()
    return


############################
# CSV関係
############################
def tsv_to_csv(tsv_path, csv_path, from_encoding=SHIFT_JIS, to_encoding=UTF_8) -> None:
    """encodingを指定してTSVファイルをCSVファイルに変換
    tsv_path: tsvのファイルパスを指定
    csv_path: csvのファイルパスを指定
    from_encoding: 変換したい
    """
    input_file = codecs.open(tsv_path, mode='r', encoding=from_encoding)
    output_file = codecs.open(csv_path, mode='w', encoding=to_encoding)

    # delimiter is tab
    data = csv.reader(input_file, delimiter='\t')
    target_file = csv.writer(output_file, delimiter=',')

    for row in data:
        target_file.writerow(row)

    input_file.close()
    output_file.close()
    return


def csv_to_dicts(csv_path, keyname_list) -> list:
    """csvファイルをlistに変換
        csv_path: csvファイルのパス
        keyname_list: dict形式のキー名
    """
    result_list = []
    with open(csv_path, mode='r', encoding=UTF_8) as f:
        # convert to dictlist
        get_list = csv.DictReader(f, keyname_list)
        for row in get_list:
            result_list.append(dict(row))
    return result_list

def csv_to_list(csv_path) -> list:
    """csvファイルを行ごとの二次元配列に変換"""
    with open(csv_path, mode='r') as f:
        two_dim_lst = csv.reader(f)
        return list(two_dim_lst)


def add_row(csv_path, val_list):
    """CSVファイルに行を追加
        csv_path: csvのファイルパス
        val_list: 行の値を配列形式で取得
    """
    with open(csv_path, 'a') as f:
        w = csv.writer(f)
        w.writerow(val_list)
    return


############################
# エクセル関係
############################
def excel_to_csv(xlsx_path, csv_path, sheet_name, usecols, index_col=0, header=0) -> None:
    """excelのsheetを指定してCSVに変換
    xlsx_path: 読み込むExcelファイルのパス
    csv_path: 書き出すCSVファイルのパス
    sheet_name: CSVに変換するExcelのシート名
    use_cols: 0始まりで列を指定
    index_col: インデックスとなる列を指定(None: どの列もインデックスとして使用しない=連番使用)
    header: ヘッダーとなる行を指定
    """
    # read sheet
    df = pd.read_excel(
        xlsx_path,
        sheet_name=sheet_name,
        usecols=usecols,
        index_col=index_col,
        header=header
    )
    df.to_csv(csv_path)
    return

def create_excel_book(book_path):
    """excelブックを作成"""
    book = exl.Workbook()
    book.save(book_path)
    return book

def add_row_to_sheet(sheet, row, val_lst) -> None:
    """シート書き込み
        row: 行番号(1始まり)
        val_lst: 行に書き込む値のリスト
    """
    try:
        for i, val in enumerate(val_lst):
            column = i+1
            sheet.cell(row=row, column=column, value=val)
    except Exception:
        pass
    return

import csv
import numpy as np
import pandas as pd
import openpyxl as excel


def main():
    # # 新規ワークブックを作る
    # wb = excel.Workbook()
    # # アクティブなワークシートを得る
    # ws = wb.active
    # # A1のセルに値を設定
    # ws['A1'] = 'こんにちは'
    # # ファイルを保存
    # wb.save('./index.xlsx')
    a1 = np.arange(2)
    idx = pd.Index(['A', 'B'], name = 'index')
    series = pd.Series(a1, index=idx)
    print(series)


if __name__ == '__main__':
    main()

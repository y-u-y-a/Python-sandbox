import csv
import pandas as pd

import libs

#########################
# 2. csvデータを振り分け(for文)
# 3. excelシートに書き込み
#########################


def main():
    file_path = './_storage/sample.csv'
    # df = pd.read_csv(file_path, usecols=[1, 2, 4, 5, 9, 10, 11])
    # for col_name, item in df.iteritems():
    #     print(col_name)
    #     print('='*20)
    #     print(item)
    # print(df.head(1))
    # # 質問の処理
    df = pd.read_csv(file_path, usecols=[12, 13, 14, 15, 16, 17, 18, 19])
    result = df[df == 9]
    print(result)
    # print(df.tail(2))


if __name__ == '__main__':
    main()

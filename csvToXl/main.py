import libs

#########################
# 2. csvデータを振り分け(for文)
# 3. excelシートに書き込み
#########################


def main():
    # tsvファイルの変換
    # [input]
    input_file = './storage/keywords.tsv'
    output_file = './storage/output.csv'
    from_encoding = libs.get_encoding(input_file)

    libs.convert_tsv(input_file, output_file, from_encoding)


if __name__ == '__main__':
    main()

    # encodingの変換
    # # [input]
    # input_file = './_sample/shift_jis.csv'
    # output_file = './storage/utf-8.csv'
    # from_encoding = libs.get_encoding(input_file)

    # libs.convert_encoding(input_file, output_file, from_encoding)

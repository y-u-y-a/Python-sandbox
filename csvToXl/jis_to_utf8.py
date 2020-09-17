import csv, codecs


def main():
    shift_jis_csv_path = './_sample/shift_jis.csv'
    utf8_csv_path = './utf8.csv'

    jis_file = codecs.open(shift_jis_csv_path, 'r', 'shift_jis')
    utf_file = codecs.open(utf8_csv_path, 'w', 'utf-8')

    for index, row in enumerate(jis_file):
        utf_file.write(row)
        # if index == 10:
        #     break

    jis_file.close()
    utf_file.close()


if __name__ == '__main__':
    main()

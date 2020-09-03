# 標準ライブラリ
import csv
# PyPIライブラリ
# 自作クラス

class File(object):

    def __init__(self):
        return

    # dict型のリストをcsvとしてエクスポートする処理
    def dictListToCsv(self, get_list: list, get_file: str) -> None:

        if not self.isDictList(get_list):
            print("dict型以外の要素が含まれています。")
            return

        with open(get_file, mode="a", encoding="utf-8") as file:

            writer = csv.writer(file)

            for target in get_list:

                # dictの中身を展開
                val_list: list = []
                for val in target.values():
                    val_list.append(val)
                    continue

                # 引数はlist型
                writer.writerow(val_list)
                continue
            return


    def isDictList(self, get_list: list) -> bool:

        for target in get_list:

            if type(target) is not dict:
                return False

        return True

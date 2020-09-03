import csv

def main():

    new_list = [[] for i in range(9)]

    with open("file/before.csv", encoding="utf-8") as f:
        # csvの行ごとの配列として返す
        reader = csv.reader(f)
        # 二次元配列取得
        for row in reader:
            index = 0
            for val in row:
                new_list[index].append(val)
                index += 1

    with open("file/after.csv", mode="a", encoding="utf-8") as f:
        # csvに書込み
        writer = csv.writer(f)
        writer.writerows(new_list)
    return

if __name__ == "__main__":
    main()

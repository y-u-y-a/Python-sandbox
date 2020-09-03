from libs import Scraping, File

def getWordList(url):

    # インスタンス生成
    scrap = Scraping.Scrap(url)

    # インスタンスメソッド実行
    en_list: list = scrap.getTextListByClass("eng")
    ja_list: list = scrap.getTextListByClass("jap")

    word_list: list = list()

    for (en, ja) in zip(en_list, ja_list):

        word: dict = { "en": en, "ja": ja }
        word_list.append(word)

    return word_list


# どこから呼び出されているか？
if __name__ == "__main__":

    # インスタンス生成
    file = File.File()

    url_list: list = [
        "https://www.eigo-duke.com/tango/chu1.html",
        "https://www.eigo-duke.com/tango/chu2.html",
        "https://www.eigo-duke.com/tango/chu3.html"
    ]

    for url in url_list:

        # 単語リスト取得
        word_list: list = getWordList(url)
        # csv書き出し
        file.dictListToCsv(word_list, "get_data.csv")

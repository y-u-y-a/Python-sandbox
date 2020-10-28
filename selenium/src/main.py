import glob

from modules.scrap import ScrapHTML


def main():
    url = 'https://job.mynavi.jp/21/pc/search/corp91256/outline.html'
    sc = ScrapHTML(url)

    # start
    h1 = sc.get_h1()
    print(h1)

if __name__ == '__main__':
    main()

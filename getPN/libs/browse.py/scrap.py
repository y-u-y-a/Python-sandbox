# import requests, time
# from bs4 import BeautifulSoup


# def get_html(url: str):
#     time.sleep(1)
#     res = requests.get(url)
#     res.encoding = res.apparent_encoding

#     html = BeautifulSoup(res.text, "html.parser")
#     return html

# def get_h1(html) -> str:
#     h1_list = html.select('h1')
#     return h1_list[0].getText()

# def get_text_list(html, tag_name) -> list:
#     el_list: list = html.select(tag_name)
#     text_list: list = [el.getText() for el in el_list]
#     return text_list

import pprint
import os, time, math, threading, re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import openpyxl as exl

from modules import conversion as cv
from modules.webdriver import Chrome


def main():
    try:
        # 1.
        mynavi_url = 'https://job.mynavi.jp/21/pc/corpinfo/displayCorpSearch/index'
        ch = Chrome()
        driver = ch.driver
        driver.get(mynavi_url)

        # 2. 業種選定
        # industry_list = [
        #     {'id': '0', 'name': 'maker'},
        #     {'id': '1', 'name': 'trading'},
        #     {'id': '2', 'name': 'retail'},
        #     {'id': '3', 'name': 'finance'},
        #     {'id': '4', 'name': 'service'},
        #     {'id': '5', 'name': 'software'},
        #     {'id': '6', 'name': 'ad'},
        #     {'id': '7', 'name': 'public'},
        # ]

        # 初期選択解除
        indst_id = 5
        driver.find_element_by_xpath('//*[@id="indGroup0"]/div/p/span[2]/a') # 業種解除
        driver.find_element_by_xpath('//*[@id="areaGroup0"]/div/p/span[2]/a') # エリア解除

        # 業種選択
        driver.find_element_by_xpath(f'//*[@id="indCategory{indst_id}"]').click() # 業種
        driver.find_element_by_xpath(f'//*[@id="indGroup{indst_id}"]/div/p/span[1]/a').click() # 全て選択
        driver.find_element_by_xpath('//*[@id="doSearchTypeIndustryArea2"]').click() # 検索
        time.sleep(2)
        s = re.split('[(/)]', driver.find_element_by_xpath('//*[@id="contentsleft"]/div[1]/div[2]/ul/li[2]/span').text)
        pagenate = int(s[2])

        for _ in range(pagenate):
            # 表示された会社数を取得
            el_list = driver.find_elements_by_class_name('boxSearchresultEach')
            time.sleep(8)
            company_list = []
            for i, _ in enumerate(el_list):
                company = {
                    'name': driver.find_element_by_xpath(f'//*[@id="corpNameLink[{i}]"]').text,
                    'link': driver.find_element_by_xpath(f'//*[@id="corpNameLink[{i}]"]').get_attribute('href')
                }
                company_list.append(company)
                print(i, company)
            driver.find_element_by_xpath('//*[@id="upperNextPage"]').click() # 次の100件へ
            time.sleep(5)
        # end
        time.sleep(5)
        driver.quit()
        return
    except Exception as e:
        print(e)
        return

if __name__ == '__main__':
    main()

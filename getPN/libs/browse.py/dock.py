import os, sys, time, datetime
# import chromedriver_binary # docker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DRIVER_PATH = os.environ['DRIVER_PATH']
CHROME_PATH = os.environ['CHROME_PATH']

class Chrome(object):

    def __init__(self, start_url):
        self.driver = self.get_driver()
        self.driver.get(start_url)

    def get_driver(self):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=ja') # configure language
        # options.binary_location = CHROME_PATH # docker
        driver = webdriver.Chrome(DRIVER_PATH, options=options)
        return driver

    def end(self) -> None:
        time.sleep(3)
        self.driver.quit()
        return None

    def get_screen_shot(self) -> None:
        dt = datetime.datetime.today()
        now = dt.strftime('%Y%m%d%H%M%S')
        self.driver.save_screenshot(f'./{now}.png')
        return None

    # by class ########################
    def get_element(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        return element

    def get_elements(self, class_name):
        elements = self.driver.find_elements_by_class_name(class_name)
        return elements

    # by xpath
    def get_element_by_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements

    def get_text_by_xpath(self, xpath) -> str:
        text = self.driver.find_element_by_xpath(xpath).text
        return text

    def get_link_by_xpath(self, xpath) -> str:
        a_tag = self.driver.find_element_by_xpath(xpath)
        link = a_tag.get_attribute('href')
        return link

    def click_by_xpath(self, xpath: str) -> None:
        time.sleep(1)
        el = self.driver.find_element_by_xpath(xpath)
        el.click()
        return None

    def xpath_wait(self, xpath) -> None:
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return None

    # by name ########################
    def get_element_by_name(self, get_name):
        element = self.driver.find_element_by_name(get_name)
        return element

    # get from element ###############
    def get_link(self, element) -> str:
        link = element.find_element_by_tag_name('a').get_attribute('href')
        return link

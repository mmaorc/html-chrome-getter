from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
import sys


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The resource url')
    args = parser.parse_args()

    url = args.url

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    with WebDriver(webdriver.Chrome(chrome_options=chrome_options)) as d:
        d.get(url)
        content = d.page_source

    sys.stdout.write(content)

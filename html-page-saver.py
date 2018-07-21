from selenium import webdriver
import argparse
import os
from datetime import datetime


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out',
                        default='./', help='The output directory')
    parser.add_argument('url', help='The resource url')
    args = parser.parse_args()

    out_dirpath = args.out
    url = args.url

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    print('Current time is {}'.format(current_time))

    out_filename = current_time + '.html'
    out_filepath = os.path.join(out_dirpath, out_filename)

    print('Getting url {}'.format(url))
    with WebDriver(webdriver.Chrome()) as d:
        d.get(url)
        content = d.page_source

    print('Saving to file {}'.format(out_filepath))
    with open(out_filepath, encoding='utf-8', mode='w') as f:
        f.write(content)

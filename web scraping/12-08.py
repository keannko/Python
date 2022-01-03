import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_source_html(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    
    driver.get(url=url)
    print(f"Current URL is:{driver.current_url}")
    time.sleep(55)
 
       

def main():
    get_source_html(url='http://earnever.ml/products')

if __name__=='__main__':
    main()
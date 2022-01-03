import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_source_html(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    try:
        driver.get(url=url)
        # print(driver.window_handles)
        print(f"Current URL is:{driver.current_url}")
        time.sleep(3)
        items = driver.find_elements_by_xpath("//*[@data-cy='listing-ad-title']")
        # items[0].click()
        # print(driver.window_handles)
        time.sleep(5)

        driver.switch_to.window(driver.window_handles[1])
        print(f"Current URL is:{driver.current_url}")
        time.sleep(5)

        username = driver.find_element_by_class_name('css-u8mbra-Text eu5v0x0')
        print(f"Username is: {username.text} ")
        time.sleep(5)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)


    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url='https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/')

if __name__=='__main__':
    main()
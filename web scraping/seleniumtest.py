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
    get_source_html(url='https://www.google.com/search?rlz=1C1CHZN_ruUA962UA962&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=AOaemvLlzG9E8LRLd0886Z7E0QL9gqc9pw:1637665250482&q=smoking+shops+and+tobacco+products+shops+in+England.&rflfq=1&num=10&sa=X&ved=2ahUKEwiv44-8qq70AhUnmYsKHTd9C_AQjGp6BAgDEGU&biw=1517&bih=694&dpr=0.9#rlfi=hd:;si:;mv:[[54.204427499999994,0.8389700999999999],[50.1989907,-5.4188562]]')

if __name__=='__main__':
    main()
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests

browser = webdriver.Chrome()

url = 'http://daum.net'

browser.get(url)

# 매물 설정
browser.find_element_by_id("q").send_keys("송파 헬리오시티")
browser.find_element_by_id("q").submit()

soup = BeautifulSoup(browser.page_source, "lxml")
rows = soup.find("table", attrs={"class" : "tbl"}).find("tbody").find_all("tr")


for idx, row in enumerate(rows):

    columns = row.find_all("td")
    print(f"======매물 {idx + 1}======")
    print()

    print(f"거래: {columns[0].get_text()}")
    print(f"면적: {columns[1].get_text()}")
    print(f"가격: {columns[2].get_text()}")
    print(f"동 : {columns[3].get_text()}")
    print(f"층 : {columns[4].get_text()}")

    print()

        
    



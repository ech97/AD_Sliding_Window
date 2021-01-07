import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)

url = 'https://auth.fastcampus.co.kr/sign-in?client_id=fc%3Aclient%3Awww&response_type=token&redirect_uri=https%3A%2F%2Fwww.fastcampus.co.kr%2F&scope=www'
url2 = 'https://www.fastcampus.co.kr/courses/201083/clips/'

browser.get(url)

browser.find_element_by_id('user-email').send_keys("ech97@konkuk.ac.kr")
browser.find_element_by_id('user-password').send_keys("!airplane9152")
browser.find_element_by_id('user-password').submit()

time.sleep(1)

browser.get(url2)

time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")
times = soup.find_all("div", attrs={"class", "fco-clip-list-item__right__info__footer"})

hour, min, sec = 0, 0, 0

for time in times:
    time_list = time.get_text().replace(" ", "").split(":")
    min += int(time_list[0])
    sec += int(time_list[1])

min += sec // 60
hour = min // 60
min = min % 60
sec = sec % 60

print(f"{hour}시간 {min}분 {sec}초 소요 예상")
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from datetime import datetime
import csv

# csv 파일 쓰기 설정 (날짜 포함)
filename = "csv/avsee_scrap_" + datetime.today().strftime("%Y.%m.%d")+".csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# selenium 옵션 설정 (headless & user-agent)
options = webdriver.ChromeOptions()

options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

# webdriver 실행
browser = webdriver.Chrome(options=options)

# 메인 사이트 url 설정
url_main = "https://avsee13.tv/"
browser.get(url_main)

# 로그인하기
browser.find_element_by_id("mb_id").send_keys("tbakzha123")
browser.find_element_by_id("mb_password").send_keys("tbakzha333")
browser.find_element_by_id("mb_password").submit()

# 스크랩 창 들어가기
url_scrap = url_main + "bbs/scrap.php?&page={}".format(1)
browser.get(url_scrap)

# 스크랩 개수 및 총 페이지 번호 확인
scrap_num = browser.find_element_by_xpath("/html/body/div/div/table/tbody/tr[2]/td[1]").text
pages = (int(scrap_num) // 15) + 1

# csv 제목 설정
title = "번호 분류 제목 링크".split()
writer.writerow(title)

# 페이지 마다 스크랩 정보 가져오기
for page in range(1, pages + 1):
    
    # 스크랩 페이지 넘기기
    url_scrap = url_main + "bbs/scrap.php?&page={}".format(page)
    browser.get(url_scrap)
    
    # bs4를 통해 데이터 가져오기
    soup = BeautifulSoup(browser.page_source, "lxml")
    rows = soup.find("table", attrs={"class":"div-table table"}).find("tbody").find_all("tr")
    
    # 로딩 구현
    print(int(page / pages * 100), "% 진행 중")

    # 가로줄 가져오기 (td)
    for row in rows: 

        # 가로줄 한줄에 들어있는 열을 리스트 형식으로 저장
        data = []

        # 모든 열 가져오기
        columns = row.find_all("td")
        
        # 열을 분리하여 data 리스트에 append 해주기
        for k, column in enumerate(columns):
            
            # 필요없은 항목(번호, 날짜, 삭제버튼) 건너뛰기
            if k == 3 or k == 4:
                continue
            
            # 데이터 가져오기
            data.append(column.get_text())
            
            # 링크 가져오기
            if k == 2:
                data.append(url_main + "bbs" + column.a["href"][1:])

        # csv에 기록
        writer.writerow(data)


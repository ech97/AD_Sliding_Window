# 시총 찾는 프로그램 제작
import csv
import requests
import re
from bs4 import BeautifulSoup


filename = "csv/시가총액1-200.csv"
# signiture의 의미인 sig를 추가해주기
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

page = 1

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

title_columns = soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")
title = [title_column.get_text() for title_column in title_columns ]
writer.writerow(title)   

for page in range(1, 5):

    # 표의 가로축 다 가져오기(table 태그 중 class 어트리뷰트 - tbody 태그 - tr 태그의 모두를 가져오기)
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        # tr 즉, 가로줄에서 td는 세로를 뜻함
        columns = row.find_all("td")

        # 특정 가로줄의 td태그, 즉 열의 개수가 1개 이하인 경우, 건너뛰기
        if len(columns) <= 1:
            continue

        # 리스트에 담은 한줄짜리 for문 / 인자로 전달되는 (\t \n같은거 제거하기위해 strip 함수)
        data = [column.get_text().strip() for column in columns]

        #list형 데이터를 넣으면 끝
        writer.writerow(data)

     
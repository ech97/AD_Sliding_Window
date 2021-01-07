# 구글 무비에서 정보 받아오기
# 할인하는 영화정보만 스크래핑 해보자
# Point: 동적 페이지 // 스크롤을 내릴때 자료가 업데이트 되는 경우


import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

# 한국어로 페이지 요청
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Accept-Language" : "ko-KR,ko"}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})


for movie in movies:
    print(movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text())


# html로 저장
with open("movies.html", "w", encoding="utf-8-sig") as f:
    f.write(soup.prettify()) #html문서를 예쁘게 나타내줌
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

""" 
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs = {"class" : "title"}) # 조건에 해당하는 '모든' element a

# class라는 속성의 값이 title인 '모~든' element "a"를 반환
for cartoon in cartoons:
    print(cartoon.get_text()) 
"""    


url2 = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res2 = requests.get(url2)
res2.raise_for_status()

soup = BeautifulSoup(res2.text, "lxml")

# 제목과 링크 가져오기
cartoons = soup.find_all("td", attrs={"class" : "title"})

for cartoon in cartoons:
    link = cartoon.a["href"]
    print(cartoon.a.get_text(), "https://comic.naver.com" + link)
    print()


# 평점 가져오기
cartoons = soup.find_all("div", attrs={"class" : "rating_type"})
total_rates = 0
for cartoon in cartoons:
    rating = cartoon.find("strong").get_text()
    print(rating)
    print()
    total_rates += float(rating)

print("평균점수: ", total_rates/len(cartoons))
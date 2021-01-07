'''
beautiful soup4 와 lxml (parser)를 이용한 크롤링
'''

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 가져온 html의 '문자'를 lxml 방식으로 parser한겨

'''
print(soup)
print(soup.title.get_text()) # html 문법 거른 순수 문자
print(soup.a) # 처음 발견되는 a 엘레먼트를 찾아 출력
print(soup.a.attrs) # a가 가지고있는 속성(attribute) 확인 가능
print(soup.a["href"]) # a가 가지고있는 속성 중 href속성의 '값' 확인 가능
'''

'''
print(soup.find("a", attrs={"class" : "Nbtn_upload"})) # a를 다 뒤져서 처음으로 class속성의 값이 Nbtn...인 element a를 찾아줘
print(soup.find(attrs={"class" : "Nbtn_upload"})) # a를 다 뒤져서 처음으로 class속성의 값이 Nbtn...인 어떤 element를 찾아줘
'''
rank1 = soup.find("li", attrs={"class" : "rank01"})
#print(rank1.a) #마찬가지로 처음발견되는 a 엘레먼트(a href... 링크)를 찾아 출력

#print(rank1.a.get_text())

#print(rank1.next_sibling.next_sibling) # 인접한 다음 형제 element로 이동

''' 인접 이동 pre/next/parent '''
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling

rank2 = rank1.find_next_sibling("li") # li태그를 기준으로 찾기때문에, 위 처럼 공백이나 개행때문에 next를 두번써줄 필요없어짐
rank3 = rank2.find_next_sibling("li")

rank2 = rank3.previous_sibling.previous_sibling # 인접한 이전 형제 element로 이동

#print(rank1.parent.get_text()) # 부모로 이동

#print(rank1.find_next_siblings("li")) # 형제들 전부를 가져옴


webtoon = soup.find("a", text="바른연애 길잡이-130")
print(webtoon.get_text())

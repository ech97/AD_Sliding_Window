# 스크롤을 계속 내려 찔금찔금 데이터 모으기

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)


# 스크롤 내리기 (with JS)
# browser.execute_script("window.scrollTo(0, 1080)")

# 현재 생성된 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 문서의 총 높이만큼 스크롤 내리기


interval = 2

# 현재 문서 높이를 가져와 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 현재 로딩된 문서 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 문서의 총 높이만큼 스크롤 내리기

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight") # 변경된 높이를 가져와 저장

    # 페이지 변화가 없으면 탈출
    if curr_height == prev_height:
        break
        
    prev_height = curr_height # 이전 페이지 높이 <- 과거 페이지 높이


# 이제 스크롤이 제일 밑으로 가 있으니, soup으로 가져와서 분석

from bs4 import BeautifulSoup

# 바로 soup 객체 만들수있음. (res.text 자료를 셀레니움으로 가져올수있으므로.)
soup = BeautifulSoup(browser.page_source, "lxml")

# 클래스명을 리스트에 담아놔서 해당하는 모든것들을 가져올수있게!
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

'''
for movie in movies:
    print()
    print(movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()) # 영화 제목 가져오기
    print(movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text()) # 영화 가격 가져오기
    print()
    print("-"*100)
time.sleep(100)
'''

for movie in movies: 

    # 할인전 가격이 존재하는애들만 필터링 하는거임! (아이디어 미쳤다...)
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})

    if original_price:

        original_price = original_price.get_text()
        curr_price = movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text()
        link = movie.find("a", attrs = {"class" : "JC71ub"})["href"] # 링크 가져오기 그냥 movie.a["href"] 써도 무방
        title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text() # 영화제목 가져오기
    
        print()

        print(f"제목: {title}") # 영화 제목 가져오기
        print("할인 전 가격", original_price[0] + " " + original_price[1:])
        print("할인 후 가격", curr_price[0] + " " + curr_price[1:])
        print(f"링크: https://play.google.com{link}")

        print()
        print("-"*100)
    else:
        continue
        

# 할인하고 있는 영화만 필터링
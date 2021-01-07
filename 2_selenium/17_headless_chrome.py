# headless 크롬 = 크롬을 키지않고, 뒤로 사용하는거 ㄱㅇㄷ
# 스크롤을 계속 내려 찔금찔금 데이터 모으기

from bs4 import BeautifulSoup
from selenium import webdriver
import time

interval = 2



# ----- 이것만 설정해주면 됨 ----- #
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # 백그라운드에서 이 크기라고 생각하고 동작
browser = webdriver.Chrome(options=options)
# 밑에 스크린샷 남기는 코드 존재 ***
# ------------------------------- #



url = "https://play.google.com/store/movies/top"
browser.get(url)


prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 문서의 총 높이만큼 스크롤 내리기

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight") # 변경된 높이를 가져와 저장

    if curr_height == prev_height:
        break
        
    prev_height = curr_height 

print("스크롤 완료")
browser.get_screenshot_as_file("imgs/google_movie.png")


soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})


for movie in movies: 

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
        

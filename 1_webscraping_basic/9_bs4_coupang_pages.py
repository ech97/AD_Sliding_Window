
'''
=== GET 방식 ===

? 변수 = 값 & 변수2 = 값2 & 변수3 = 값3
: 물음표 뒤에 변수와 값이 &로 묶여있음


=== POST 방식 ===

좀 더 숨겨서 전송
: 주소가 바뀌지않는경우는 POST정보

'''

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

for i in range(1, 6):



    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)    print("\n====== 페이지:", i, "======")
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class", re.compile("^search-product")}) # search-product로 시작하는 애들 다 불러옴

    for item in items:

        # 광고제품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print(" <광고 상품은 제외했습니다>\n\n")
            continue

        name = item.find("div", attrs={"class" : "name"}).get_text()

        if "Apple" in name:
            #print(" <Apple 상품을 제외했습니다>\n\n")
            continue

        price = item.find("strong", attrs={"class" : "price-value"}).get_text() #가격
        rate = item.find("em", attrs={"class" : "rating"}) #평점
        rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})
        #link = item.find("a", attrs={"class":"search-product-link"})["href"]
        link = item.a["href"]
        # rate, rate_cnt 없는 애들 거르기
        if rate:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()[1:-1]

            # review 100개 이상 평점 4.5 이상
            if float(rate) < 4.5 or int(rate_cnt) < 100 :
                continue
        else:
            continue
            #rate, rate_cnt = None, None
            
        print(f"\n제품명 : {name}")
        print(f"가격: {price}")
        print(f"평점: {rate} \t 평점 수: ({rate_cnt})")
        print(F"링크: https://coupang.com{link}\n")
        print("-"*100)
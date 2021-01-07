'''
[오늘의 날씨]
흐림, 어제보다 ㅐㅐ 높아요
현재 ㅐㅐ도 (최저 ㅐㅐ / 최고 ㅐㅐ)
오전 강수확률 ㅐㅐ /오후 강수확률 ㅐㅐ

미세먼지 ㅐㅐ 좋음
초미세먼지 ㅐㅐ 좋음
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def scrape_weather():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    print("[오늘의 날씨]")

    # 현재보다 ㅐㅐ 높아요
    print(soup.find("p", attrs={"class":"cast_txt"}).get_text())
    
    # 현재 날씨
    print(soup.find("span", attrs={"class":"todaytemp"}).get_text())

    # 최저/최고 기온
    print(soup.find("span", attrs={"class":"min"}).get_text())
    print(soup.find("span", attrs={"class":"max"}).get_text())


    # 강수확률
    prain = soup.find_all("span", attrs={"class":"num"})
    prain_am = prain[0].get_text()
    prain_pm = prain[1].get_text()

    print(f"{prain_am}% {prain_pm}%")

    # 미세먼지
    print(soup.find("dd", attrs={"class":"lv2"}).get_text())
    print(soup.find("dd", attrs={"class":"lv3"}).get_text())

    # 미세먼지 찾는 방법 upgrade
    dust = soup.find("dl", attrs={"class":"indicator", "id":"dust"}) # 두가지 조건을 걸거나
    dust = soup.find("dl", attrs={"class":"indicator"}, text=["미세먼지", "초미세먼지"]) # text를 중심으로 찾을수도있음




if __name__ == "__main__":
    scrape_weather()

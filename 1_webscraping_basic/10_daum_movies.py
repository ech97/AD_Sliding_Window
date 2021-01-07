import requests
import re
from bs4 import BeautifulSoup


for year in range(2015,2020):

    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    imgs = soup.find_all("img", attrs={"class": "thumb_img"})
    for idx, img in enumerate(imgs):
        img_url = img["src"]

        # //로 문자열이 시작한다면
        if img_url.startswith("//"):
            img_url = "https:"+img_url

        print(img_url)

        img_res = requests.get(img_url)
        img_res.raise_for_status()

        # text파일이 아니므로, wb로 저장
        with open("imgs/{}movie{}.jpg".format(year, idx+1), "wb") as f:
            # 리소스가 가지고있는 content 정보를 바로 파일로 쓰는겨
            f.write(img_res.content)

        # 상위 5개 항목만 가져올거임
        if idx >= 4:
            break
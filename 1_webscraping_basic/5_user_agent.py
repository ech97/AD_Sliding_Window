# 헤더를 통해서 이 사람이 모바일인지 PC인지 프로그램인지 확인함
# 이 때문에 403오류가 발생하기도 하는데
# 이를 해결하기위해서 User agent string 검색해서 지금 접속한 브라우저 및 PC/모바일 정보를 담은 헤더를 복사

import requests

url = "http://wein.konkuk.ac.kr"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

res = requests.get(url, headers=headers) # PC + 크롬의 헤더를 이용하여 request
res.raise_for_status()

with open("webscraping_basic/nadocoding.html", "w", encoding = 'utf8') as f:
    f.write(res.text)
import requests

res = requests.get("http://wein.konkuk.ac.kr")

"""
print("응답코드 :", res.status_code) # 200이면 정상, 403이면 접근권한x

if res.status_code == requests.codes.ok: #ok == 200
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드: ", res.status_code, "]")
"""

res.raise_for_status() #문제가 발생하는경우 에러내고 프로그램 종료


with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
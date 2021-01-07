from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import pyautogui
import time
import sys

'''
1. 실행을 위해 본인 크롬버전에 맞는 Chrome Driver.exe 를 Python 파일이 있는 폴더안에 동봉

2. Python 설치 이후 프롬프트 창에서 다음과 같은 명령어 실행 필요

pip install selenium
pip install pyautogui


3. 프롬프트 창에서 cd 명령어를 통해 Python 파일이 있는 경로로 이동한 뒤 다음과 같이 실행

python Unistudy.py [시작 강의 번호(1부터 시작)] [마지막 강의 번호]
ex) python Unistudy.py 1 10
'''

#--------Param--------#
# Player Delay Time
PDT = 10

# Extra Lecture Waiting
ELW = 15

# Lecture num
start_Lecture = 2
final_Lecture = 24

try:
    start_Lecture = int(sys.argv[1])
except IndexError:
    print()
try:
    final_Lecture = int(sys.argv[2])
except IndexError:
    print()
#---------------------#

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)

url = 'https://www.unistudy.co.kr/member/memb_login.asp'
url2 = 'https://www.unistudy.co.kr/mypage/Room/Lec_Movie_Dtl.asp?app_seq=96646'

browser.get(url)

browser.find_element_by_name('input_id').send_keys("noonggoong69")
browser.find_element_by_name('input_pw').send_keys("noonggoong74a+")
browser.find_element_by_name('input_pw').submit()

browser.get(url2)

for idx in range(start_Lecture, final_Lecture + 1):
        
    # 몇 분인지 따오기
    min_str = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[{}]/td[4]".format(idx)).text.replace("분", "")

    min = int(min_str)
    sec = min * 60
    sec_extra = sec + ELW

    # 고화질 버튼 클릭
    browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[{}]/td[3]/i[2]".format(idx)).click()

    time.sleep(2)

    # 처음부터 보기 클릭
    try:
        no_continue = browser.find_element_by_xpath("/html/body/article/div/div[2]/div/div/div/div[2]/div/a[1]")
        no_continue.click()

    except NoSuchElementException:  
        print()
    # delay 대기
    time.sleep(PDT)

    # click the space bar
    pyautogui.press('space')
    time.sleep(1.5)
    pyautogui.press('enter')


    # 강의 시간 만큼 대기
    time.sleep(sec + ELW)
    
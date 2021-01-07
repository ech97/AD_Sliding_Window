import time
from selenium import webdriver
browser = webdriver.Chrome()


# 창 최대화
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("27")[0].click() #이번달 27 선택
browser.find_elements_by_link_text("28")[0].click() #이번달 28 선택

time.sleep(0.5)
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
browser.find_element_by_link_text('항공권 검색').click()



# 검색 후 로딩시간을 고려해줘야함
# 최대 10초동안 기다리고 그 전에 특정한 애가 로딩이되면 바로 실행해

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    # 튜플형태로 XPath값 삽입
    print(elem.text)
except:
    browser.quit()



# 첫번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)
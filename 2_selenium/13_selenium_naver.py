# 네이버 로그인

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

time.sleep(random.uniform(1,3))


#elem에 저장해서 두고두고 클릭하거나 키입력 등 후처리를 하지않을거니깐 걍 바로 뒤에 send_key 붙이기
browser.find_element_by_id("id").send_keys("ech97")
browser.find_element_by_id("pw").send_keys("")
browser.find_element_by_id("log.login").click()
#browser.find_element_by_id("pw").submit() 으로 클릭 대체가능

# 기존에 들어가있던 값 지우기
browser.find_element_by_id("id").clear()


# 자동완성 원리를 이용하여 recapcha 우회

input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "ech97", pw = "??")

time.sleep(random.uniform(1,3))
browser.execute_script(input_js)

time.sleep(random.uniform(1,3))
browser.find_element_by_id("log.login").click()


# html 정보 출력
print(browser.page_source)

browser.quit()

exit()

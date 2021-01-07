from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://naver.com")

# bs4의 find함수와 유사
elem = browser.find_element_by_class_name("link_login")
print(elem)

# 클릭
elem.click()

# 이전페이지 등 동작
browser.back()
browser.forward()
browser.back()
browser.refresh()
# 페이지 변경 후에는 element 재선언 필수

elem = browser.find_element_by_class_name("input_text")

# key 입력하는 툴 가져오기
from selenium.webdriver.common.keys import Keys
elem.send_keys("ech97")
elem.send_keys(Keys.ENTER)

# a 태그 관련된거 처음것만 가져오기
elem = browser.find_element_by_tag_name("a")

# a 태그 관련하여 전부 가져오기
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    # attrs의 값 가져오기 가능
    e.get_attribute("href")

browser.get("http://daum.net")
elem = browser.find_element_by_name("q") 
elem.send_keys("이찬현")
elem.send_keys(Keys.ENTER)
browser.back()

elem = browser.find_element_by_name("q") 

# 검색 버튼을 누르기 위해 버튼의 Xpath를 Copy
# //*[@id="daumSearch"]/fieldset/div/div/button[2]
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

# 탭 하나 종료
browser.close()

# 모든 탭 종료 
browser.quit()

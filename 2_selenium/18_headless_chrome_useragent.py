# headless chrome은 useragent가 바뀌기 때문에, 사이트에서 알고 차단할수있음
# 추가자료는 selenium with python 검색해서 찾아보기


from bs4 import BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# useragent를 변경하기위해 다음을 추가!!!!!!!!!!!!!!!!!!!!!!!!!!!!
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")


browser = webdriver.Chrome(options=options)


# 사이트에서 나의 user-agent 정보를 가져오기
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()
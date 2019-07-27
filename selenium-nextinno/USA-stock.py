from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome('/Users/jung/development/projects/python/glof-crawling/python_test/selenium-nextinno/chrome-driver/chromedriver75')
driver.implicitly_wait(3)
driver.get('https://www.kiwoom.com/nkw.templateFrameSet.do')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="id"]').send_keys('rsjung')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('fotjd12')
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="m1304010000_login"]').click()

# Naver 페이 들어가기
# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = BS(html, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')

# for n in notices:
#     print(n.text.strip())

# //*[@id="id"]
from selenium import webdriver
from bs4 import BeautifulSoup as BS

driver = webdriver.Chrome('/Users/jung/development/projects/python/glof-crawling/python_test/selenium-nextinno/chrome-driver/chromedriver75')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('mcthemaxrs')
driver.find_element_by_name('pw').send_keys('gksdid2012')
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BS(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())
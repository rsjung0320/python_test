# https://globalmonitor.einfomax.co.kr/kw_usa_em.html?searchtype=all&searchtext=&startdate=20190430&enddate=20190730&seldate=sel#/

# from selenium import webdriver
# from bs4 import BeautifulSoup as BS

# driver = webdriver.Chrome('selenium-nextinno\chrome-driver\chromedriver.exe')
# driver.implicitly_wait(10)

# # Naver 페이 들어가기
# # headers = {
# # 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
# # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# # 'Accept-Encoding': 'gzip, deflate, br',
# # 'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
# # 'Cache-Control': 'max-age=0',
# # 'Connection': 'keep-alive',
# # 'Cookie': '_ga=GA1.3.137300354.1564482531; _gid=GA1.3.580146333.1564482531',
# # 'Host': 'globalmonitor.einfomax.co.kr',
# # 'Upgrade-Insecure-Requests': '1',
# # 'If-Modified-Since': 'Fri, 01 Feb 2019 07:08:48 GMT',
# # 'If-None-Match': '"4348-1549004928511"'
# # }
# driver.get('https://globalmonitor.einfomax.co.kr/kw_usa_em.html?searchtype=all&searchtext=&startdate=20190430&enddate=20190730&seldate=sel#/1/1/board/page=1')
# html = driver.page_source
# soup = BS(html, 'html.parser')
# # notices = soup.select('div.p_inr > div.p_info > a > span')
# print(soup)


import requests
import time
from bs4 import BeautifulSoup as BS

# url = 'https://www.lpga.or.jp/members/info/1000932'
url = 'https://globalmonitor.einfomax.co.kr/kw_usa_em.html?searchtype=all&searchtext=&startdate=20190430&enddate=20190730&seldate=sel#/1/1/board/page=1'

#test
#html = urllib.request.urlopen(url)
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ga=GA1.3.137300354.1564482531; _gid=GA1.3.580146333.1564482531',
'Host': 'globalmonitor.einfomax.co.kr',
'Upgrade-Insecure-Requests': '1',
'If-Modified-Since': 'Fri, 01 Feb 2019 07:08:48 GMT',
'If-None-Match': '"4348-1549004928511"'
}
html = requests.get(url, headers=headers).text
time.sleep(5)

soup = BS(html, 'html.parser')
time.sleep(5)
# soup.html.findAll(text=True, recursive=False) 
print(soup)
# TmtPerformance = soup.find('div', {'class': 'TmtPerformance record'})

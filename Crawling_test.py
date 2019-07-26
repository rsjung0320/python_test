# 웹 크롤링(Web Crawling)
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

# 1. 웹 문서 전체가 출력됩니다. 
# html = urlopen("http://www.naver.com")  
# bsObject = BS(html, "html.parser") 
# print(bsObject) # 웹 문서 전체가 출력됩니다. 

# 2. title 출력
# html = urlopen("http://www.naver.com")
# bsObject = BS(html, "html.parser")
# print(bsObject.head.title)

# # 3. 모든 메타 데이터의 내용 가져오기
# html = urlopen("https://www.python.org/about")
# bsObject = BS(html, "html.parser")
# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))

# # 4. 원하는 태그의 내용 가져오기 
# print (bsObject.head.find("meta", {"name":"description"}))
# print (bsObject.head.find("meta", {"name":"description"}).get('content'))

# 5. 모든 링크의 텍스트와 주소 가져오기
html = urlopen("https://www.naver.com")
bsObject = BS(html, "html.parser")

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
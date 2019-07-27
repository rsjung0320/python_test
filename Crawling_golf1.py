import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.lpga.or.jp/members/info/1000932'

#html = urllib.request.urlopen(url)
html = requests.get(url).text

soup = BS(html, 'html.parser')
soup.html.findAll(text=True, recursive=False) 

placeholders = soup.find('table', {'class': 'tournamentRecordTable pCol3'})
tournamentRecordTable_thead = placeholders.find('thead')
tournamentRecordTable_thead_th = tournamentRecordTable_thead.find('tr').find_all('th')
tournamentRecord_thead_str = ''

for i in tournamentRecordTable_thead_th:
    tournamentRecord_thead_str += i.text + ','

tournamentRecord_thead_str = tournamentRecord_thead_str[:-1] + '\n'

tournamentRecordTable_tbody = placeholders.find('tbody')
tournamentRecordTable_tbody_tr = tournamentRecordTable_tbody.find_all('tr')

tournamentRecord_tbody_str = ''

for i in tournamentRecordTable_tbody_tr:
    tournamentRecordTable_tbody_tr_td = i.find_all('td')
    for j in tournamentRecordTable_tbody_tr_td:
        tournamentRecord_tbody_str += j.text + ','
    tournamentRecord_tbody_str = tournamentRecord_tbody_str[:-1] + '\n'

print('===========================================')
print(tournamentRecord_thead_str + tournamentRecord_tbody_str)
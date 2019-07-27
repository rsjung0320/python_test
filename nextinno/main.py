import requests
from bs4 import BeautifulSoup as BS
import libs.Crawling_lllpga as CL

# url = 'https://www.lpga.or.jp/members/info/1000932'
url = 'https://www.lpga.or.jp/members/info/1000932/2019'


#html = urllib.request.urlopen(url)
html = requests.get(url).text

soup = BS(html, 'html.parser')
# soup.html.findAll(text=True, recursive=False) 

TmtPerformance = soup.find('div', {'class': 'TmtPerformance record'})
TmtPerformance_h4 = TmtPerformance.find_all('h4')
tour_list = []

for tour in TmtPerformance_h4:
    tour_list.append(tour.text.strip())

tournamentRecord_thead_str = ''

if(len(tour_list) > 1):
    placeholders = soup.find_all('table', {'class': 'tournamentRecordTable pCol3'})
    tournamentRecord_thead_str = CL.getTournamentRecordAllTable(placeholders)
else:
    placeholders = soup.find('table', {'class': 'tournamentRecordTable pCol3'})
    if(tour_list[0] == 'LPGAツアー'):
        tournamentRecord_thead_str = 'LPGAツアー' + '\n'
        tournamentRecord_thead_str += CL.getTournamentRecordTable(placeholders)
    else:
        tournamentRecord_thead_str = 'ステップ・アップ・ツアー' + '\n'
        tournamentRecord_thead_str += CL.getTournamentRecordTable(placeholders)

print(tournamentRecord_thead_str)
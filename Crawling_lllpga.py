def getTournamentRecordAllTable(tournamentRecord):
    tournamentRecord_result = ''
    
    idx = 0
    for i in tournamentRecord:
        tournamentRecord_thead_str = ''
        tournamentRecord_tbody_str = ''
        if(idx == 0):
            tournamentRecord_thead_str += 'LPGAツアー\n'
        elif(idx == 1):
            tournamentRecord_thead_str += 'ステップ・アップ・ツアー\n'

        idx += 1
        tournamentRecordTable_thead = i.find('thead')
        tournamentRecordTable_thead_th = tournamentRecordTable_thead.find('tr').find_all('th')

        for j in tournamentRecordTable_thead_th:
            tournamentRecord_thead_str += j.text + ','

        tournamentRecord_thead_str = tournamentRecord_thead_str[:-1] + '\n'
        # print(tournamentRecord_thead_str)

        tournamentRecordTable_tbody = i.find('tbody')
        tournamentRecordTable_tbody_tr = tournamentRecordTable_tbody.find_all('tr')

        for i in tournamentRecordTable_tbody_tr:
            tournamentRecordTable_tbody_tr_td = i.find_all('td')
            for j in tournamentRecordTable_tbody_tr_td:
                tournamentRecord_tbody_str += j.text + ','
            tournamentRecord_tbody_str = tournamentRecord_tbody_str[:-1] + '\n'
        
        tournamentRecord_result += tournamentRecord_thead_str + tournamentRecord_tbody_str + '\n'
    tournamentRecord_result = tournamentRecord_result[:-1]
    return tournamentRecord_result


def getTournamentRecordTable(tournamentRecord):
    tournamentRecord_result = ''
    tournamentRecord_thead_str = ''
    tournamentRecord_tbody_str = ''

    tournamentRecordTable_thead = tournamentRecord.find('thead')
    tournamentRecordTable_thead_th = tournamentRecordTable_thead.find('tr').find_all('th')

    for j in tournamentRecordTable_thead_th:
        tournamentRecord_thead_str += j.text + ','

    tournamentRecord_thead_str = tournamentRecord_thead_str[:-1] + '\n'
    # print(tournamentRecord_thead_str)

    tournamentRecordTable_tbody = tournamentRecord.find('tbody')
    tournamentRecordTable_tbody_tr = tournamentRecordTable_tbody.find_all('tr')

    for x in tournamentRecordTable_tbody_tr:
        tournamentRecordTable_tbody_tr_td = x.find_all('td')
        for y in tournamentRecordTable_tbody_tr_td:
            tournamentRecord_tbody_str += y.text + ','
        tournamentRecord_tbody_str = tournamentRecord_tbody_str[:-1] + '\n'
    
    tournamentRecord_result += tournamentRecord_thead_str + tournamentRecord_tbody_str

    return tournamentRecord_result

#################################################################################################

import requests
from bs4 import BeautifulSoup as BS

# url = 'https://www.lpga.or.jp/members/info/1000932'
url = 'https://www.lpga.or.jp/members/info/1000932/2019'


#html = urllib.request.urlopen(url)
html = requests.get(url).text

soup = BS(html, 'html.parser')
soup.html.findAll(text=True, recursive=False) 

TmtPerformance = soup.find('div', {'class': 'TmtPerformance record'})
TmtPerformance_h4 = TmtPerformance.find_all('h4')
tour_list = []

for tour in TmtPerformance_h4:
    tour_list.append(tour.text.strip())

tournamentRecord_thead_str = ''

if(len(tour_list) > 1):
    placeholders = soup.find_all('table', {'class': 'tournamentRecordTable pCol3'})
    tournamentRecord_thead_str = getTournamentRecordAllTable(placeholders)
else:
    placeholders = soup.find('table', {'class': 'tournamentRecordTable pCol3'})
    if(tour_list[0] == 'LPGAツアー'):
        tournamentRecord_thead_str = 'LPGAツアー' + '\n'
        tournamentRecord_thead_str += getTournamentRecordTable(placeholders)
    else:
        tournamentRecord_thead_str = 'ステップ・アップ・ツアー' + '\n'
        tournamentRecord_thead_str += getTournamentRecordTable(placeholders)

print(tournamentRecord_thead_str)



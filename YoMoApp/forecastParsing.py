# python -m pip install kafka-python으로 설치해야 함
from kafka import KafkaProducer

import csv
import time

producer = KafkaProducer(bootstrap_servers=['node1.sqm.private:6667'])

# TODO 4개의 값을 로드해서 다 보낸다.
f = open('C:/nable/dev/python/lecture/YoMoApp/72prediction.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

# TODO 그렇다면 row의 수는 동일하니 for문에서 rowcount로 한다.
# row 카운트
# row_count = sum(1 for row in rdr)
# print(row_count)

for line in rdr:
  # TODO csv를 통계 포맷으로 만들어야 함.
  print(line)
  # 1분으로 변경해야 함
  time.sleep(5)
  # TODO kafka produce로 넣는다.

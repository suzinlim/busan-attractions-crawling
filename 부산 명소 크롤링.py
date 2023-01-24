import requests
from bs4 import BeautifulSoup
import openpyxl

wb=openpyxl.Workbook()

ws=wb.active
ws.append(["장소", "평점", "리뷰수", "소개글"])

url = 'https://www.google.com/travel/things-to-do?g2lb=4597339%2C4667459%2C4644488%2C4596364%2C4605861%2C4419364%2C4641139%2C2502548%2C2503781%2C4624411%2C4518326%2C2503771%2C4401769%2C4306835%2C4640247%2C4258168%2C4371335%2C4317915%2C4270442%2C4679298%2C4284970%2C4291517%2C4270859&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hv7l&dest_state_type=main&dest_src=ts&q=%ED%95%9C%EA%B5%AD%20%EA%B4%80%EA%B4%91%20%EB%AA%85%EC%86%8C%20top%2010&sa=X&ved=2ahUKEwiK9Pm1hdn0AhXcr1YBHTKMBBMQuL0BegQIAxA-&tcfs=EhsKCC9tLzBodjdsEg_rtoDsgrDqtJHsl63si5w'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
    
data = soup.select("div.GwjAi")

for i in data:
    place = i.select_one("div.rbj0Ud div").text.strip() # 장소
    score = i.select_one("div.tP34jb span.KFi5wf.lA0BZ").text.strip() # 평점
    cnt_review = i.select_one("div.tP34jb span.jdzyld.XLC8M").text.strip() # 리뷰수
    info = i.select_one("div.nFoFM").text.strip() # 소개글

    ws.append([place, score, cnt_review, info])
    
wb.save("부산 명소.xlsx")
import csv
from openpyxl import Workbook

# CSV 파일에서 데이터 읽기
with open('public/poly2023_2.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active

# 데이터를 엑셀 시트에 쓰기
for row in data:
    ws.append(row)

# 엑셀 파일 저장
wb.save('poly20232.xlsx')
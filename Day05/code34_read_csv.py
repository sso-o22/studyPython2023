# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv

fileName = 'busanbus.csv'
dirName = 'C:/Source/studyPython2023/'  # 마지막에 / 꼭 적어줘야 함
fullpath = dirName + fileName

file = open(fullpath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)

file.close()  # 반드시 닫아주세요!
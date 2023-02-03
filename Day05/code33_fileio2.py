# 파일 읽어오기
file = open('./Day05/sample05.txt', 'r', encoding='utf-8')  # r = 읽기 모드

while True:
    text = file.read()  # 한줄씩 읽음 -> 반복문 사용 -> 전체 읽음

    if not text: break

    print(text)

file.close()  # file open하면 반드시 close해야함!
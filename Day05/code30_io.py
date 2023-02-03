# 입출력
number = int(input('수를 입력하세요 > '))
print(number * 5)  
# 500이 나오는 것이 아니라 100이 5번 나옴
# 모든 입력은 문자로 인식 -> int형으로 바꿔 주어야 함.

print('Life ' 'is ' 'short')
print('Life', 'is', 'short')

a = [1,2,3,4]
for i in a:
    print(i, end=' ')
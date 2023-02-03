# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b  # 실제적으로 오류가 난 곳

try:  
    x, y = input('두 수를 입력하세요 > ').split()  # split한것을 한번에 int로 묶을 수 X
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()  # 입력 실패하면 더 이상 진행 안되도록!
finally:
    print('계속되나요?')  # 이거 실행뒤 종료됨

# # 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')  # 나누기는 안하더라도 +, * 는 해야함
#     exit()

print('계산 테스트')
try:
    print(div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나누면 안돼요!') 
except Exception as e:  # 이름 길어서 e라는 별명 부여 / Exception은 부모이므로 제일 마지막에!!!
    print(e) 
finally:
    print('계산은 계속됩니다!!')  # 예외가 나든 안나든 무조건 나옴


print(add(x, y))
print(mul(x, y))

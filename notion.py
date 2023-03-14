# 라이프 스코프
a = 1  # 변수

def vartest(x):  # 함수 안에 있는 변수는 매개변수 -> 해당 함수에서만 동작
    global a  # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다
    a = a + x + 1
    return a

a = vartest(a)  # 그냥 변수
print(a)
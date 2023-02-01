# 함수
# 함수정의 - 이건 실행이 아님

# 1. 파라미터O 리턴O
def add(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result

# 함수호출, 함수의 순서는 상관X
val = add(1024, 5)
print(val)  

val = sub(1024, 1000)
print(val)  

val = mul(1024, 2)
print(val)  

val = div(1024, 10)
print(val)  
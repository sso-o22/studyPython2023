# 함수 만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴X
# 3. 파라미터X 리턴O
# 4. 파라미터X 리턴X

# 2. 파라미터O 리턴X
def add(x, y):
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

# 4. 파라미터X 리턴X
def hello():
    print('Hello~!!!')
    
# 3. 파라미터X 리턴O
def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수호출
hello()
print(hello2())

add(1024, 5)
sub(1024, 1000)
mul(1024, 2)
div(1024, 10)
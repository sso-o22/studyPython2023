# 자료형
# None 값이 없는 값
None # 컴퓨터왈 난몰라

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3  
print(type(val))  # int

val = 3.14  
print(type(val))  # float

val = 'Hello'  
print(type(val))  # str

val = 0b1010  
print(type(val))  # 2진수 -> int

val = 12.45546564643434545445434643
print(type(val))  # float

val = 4_520_000 
print(val)  # 4520000

val = 3_099.00
print(val)  # 3099.0

# 문자열
val = 'Life is short, You need Python.'
print(val)
print(type(val))

val = 'Hell\nWorld!'  # 탈출문자 / enter
print(val)
val = 'Hell\tWorld'  # tap
print(val)
val = 'Hell\t\bWorld'  # tap, 한칸 앞
print(val)  

val = '''Life is short, 
You need Python'''  # ''' 줄 바꿔서 쓴것 그대로 출력, \n보다 편함
print(val)
val = "Hi, I'm 'Soojung'"  # ''보다 에너지 낭비 -> shift 눌러야함
print(val)
val = 'Hi, I\'m \'Soojung\''  # 홑따옴표 안에 홑따옴표 쓸 때 -> 앞에 \ 쓰기
print(val)

# 불린형 or 불형
참 = True  # true -> x, t 대문자로 쓰기
거짓 = False
print(type(거짓))
print(1 + 1 == 2)  # True

# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)  # False
print(거짓 == False)  # True
print(거짓 is False)  # True

print(bool(1))  # 1 == True
print(bool(0))  # 0 == False
print(bool(3))  # 1이외 값은 True라고 하지마세요.
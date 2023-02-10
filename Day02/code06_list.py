# 복합형

# 리스트 안쓰면 
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10  # 변수 10개 만들어야함

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# 리스트 == 배열
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World!', True]
print(arr3)
print(type(arr3))

arr4 = []   # 빈 리스트
arr5 = list()  # 빈 리스트
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

# tuple1.append(4)  # tuple은 값을 넣을 수 없음, 값이 바뀌면 안될 때 사용
# print(tuple1)
print(type(tuple1))

# 딕셔너리
spiderman = { 'name' : 'Peter Parker',
               'age' : 18,
            'weapon' : 'Web Shooter',
            'deserter' : '탈영병' }  # 여러줄로 사용해도 됨

print(spiderman)
print(spiderman['weapon'])  # Web Shooter
print(spiderman['deserter'])
print(type(spiderman))

# 집합
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")  # 집합은 중복 X
print(set1)  # Hello World가 다 분해, 중복 X, 스페이스도 값이므로 나옴
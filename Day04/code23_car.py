import os
import code

# 자동차 클래스
class Car:
    __number = '54라 9538'

    def get_number(self) -> str:  # -> str 는 생략해도 됨
        return self.__number

    # 클래스 외부에선 변경X, 멤버함수로는 내부를 조작O
    def set_number(self, number):
        self.__number = number

    def __init__(self, number='54라 9538') -> None:
        print('__init__')
        self.__number = number

    # def __new__(cls):
    #     print('__new__')  # __init__ 보다 먼저 생성됨
    #     return super().__new__(cls)  # 부모클래스(상속) / super라는 클래스 생성자

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'  

yourcar = Car('88호 7486')
print(yourcar)
yourcar.__number = '54라 9999'  # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는요, 아이오닉이고, 번호가 {mycar.get_number()} 에요.')

mycar.__number = '132거 8874'
print(mycar.get_number())
print(mycar)

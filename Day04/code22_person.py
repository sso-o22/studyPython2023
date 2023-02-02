# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self) -> None:  # 생성자
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None:  
        self.name = name  # 초기화
        self.height = height
        self.gender = gender
        

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):  # class 안에 있는 함수는 self 써야함
        if option == 'Fast':
            self.walk()  # 함수안에서도 함수 실행 가능
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'
         

# Person이라는 클래스로 soojung이라는 객체 만든다
soojung = Person('최수정', 157, 'female')  # 객체생성 instance
#soojung.name = '최수정'
#soojung.height = '157'
#soojung.gender = 'female'
#soojung.blood_type = 'RH+ B'

print(f'{soojung.name}의 혈액형은 {soojung.blood_type}입니다.')

soojung.run('Fast')  
print(soojung)

# 1. 초기화 후 객체생성 
hong = Person()
hong.run('Slow')
print(hong)

print('===========================================================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')  # 클래스를 생성하는 생성자 함수와 같음
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)

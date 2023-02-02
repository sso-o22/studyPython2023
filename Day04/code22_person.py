# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    def walk(self):
        print('걷습니다.')

    def run(self, option):  # class 안에 있는 함수는 self 써야함
        if option == 'Fast':
            self.walk()  # 함수안에서도 함수 실행 가능
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print('멈춥니다.')
        

soojung = Person()  # person이라는 클래스로 soojung이라는 객체 만든다 -> 객체를 instance
soojung.name = '최수정'
soojung.height = '157'
soojung.gender = 'female'
soojung.blood_type = 'RH+ B'

print(f'{soojung.name}의 혈액형은 {soojung.blood_type}입니다.')

soojung.run('Fast')  


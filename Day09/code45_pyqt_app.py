# 템플릿 소스 : 가장 기본이 되는 소스
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):  # QWidget 상속받아서 클래스 만들거야
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # self.move(0, 0)  # 윈도우창 생기는 위치, 좌표 정수로 입력, 왼쪽위 꼭짓점이 기준
        # self.move(1440 // 2 - 200, 900 // 2 -100)  # 정중앙 위치 잡기(선생님 컴퓨터 기준)
        self.resize(400, 200)
        self.show()  # 핵심!! 없으면 아무것도 안나옴

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

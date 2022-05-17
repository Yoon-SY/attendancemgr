# Copyright 2022 Yoon Sung-Yong
# Free use in Daewon Foreign Language High School only
# NIHONGOKA SAIKOU!

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import datetime as dt

form_class = uic.loadUiType("panel.ui")[0]

# Reads txt file and returns the content as list
# Each element represents each line of the file
# Imported from Project guiyajamgr
def fileanalyze(f):
    ret = []
    while True:
        s = f.readline()
        if s == '':
            return ret
        ret.append(s)

def ppint(n):
    return str(n).rjust(2, "0")

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Numerous attendance buttons
        self.std_btn_01.clicked.connect(self.update)
        self.std_btn_02.clicked.connect(self.update)
        self.std_btn_03.clicked.connect(self.update)
        self.std_btn_04.clicked.connect(self.update)
        self.std_btn_05.clicked.connect(self.update)
        self.std_btn_06.clicked.connect(self.update)
        self.std_btn_07.clicked.connect(self.update)
        self.std_btn_08.clicked.connect(self.update)
        self.std_btn_09.clicked.connect(self.update)
        self.std_btn_10.clicked.connect(self.update)
        self.std_btn_11.clicked.connect(self.update)
        self.std_btn_12.clicked.connect(self.update)
        self.std_btn_13.clicked.connect(self.update)
        self.std_btn_14.clicked.connect(self.update)
        self.std_btn_15.clicked.connect(self.update)
        self.std_btn_16.clicked.connect(self.update)
        self.std_btn_17.clicked.connect(self.update)
        self.std_btn_18.clicked.connect(self.update)
        self.std_btn_19.clicked.connect(self.update)
        self.std_btn_20.clicked.connect(self.update)
        self.std_btn_21.clicked.connect(self.update)
        self.std_btn_22.clicked.connect(self.update)
        self.std_btn_23.clicked.connect(self.update)
        self.std_btn_24.clicked.connect(self.update)
        self.std_btn_25.clicked.connect(self.update)
        self.std_btn_26.clicked.connect(self.update)
        self.std_btn_27.clicked.connect(self.update)
        self.std_btn_28.clicked.connect(self.update)
        self.std_btn_29.clicked.connect(self.update)
        self.std_btn_30.clicked.connect(self.update)

        # Load Button
        self.loadbtn.clicked.connect(self.load)

        # Save Button
        #self.savebtn.clicked.connect(self.save)

    def update(self):
        epoch = dt.datetime.now()
        for i in range(1, 31):
            num = ppint(i)
            exec(f"if self.std_btn_{num}.isChecked() and (not self.std_time_{num}.text()): self.std_time_{num}.setText(':'.join([ppint(epoch.hour), ppint(epoch.minute), ppint(epoch.second)]))")

    def load(self): # Imported from guiyajamgr but edited
        stage = 0; text = []
        try:
            # Load file
            fname = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files(*)", "")
            if fname[0]:
                text = fileanalyze(open(fname[0], encoding="utf-8"))
            else:
                raise FileNotFoundError
            stage = 1 # Debug CP
            # FileNotFoundError is exception-handled below

            # Assigns each value
            name = [*map(str,text[4][3:].replace(':','').lstrip().split(', '))]
            stage = 2
            # IndexError in case of illegal data input, and
            # ValueError in case of indentation problem are exception-handled below

            for i in range(1, 31):
                num = ppint(i)
                exec(f"self.std_btn_{num}.setChecked(False)")
                exec(f"self.std_time_{num}.setText('')")
            stage = 3

            for i in range(1, len(name)+1): # Names
                num = ppint(i)
                # Un-hide present students and changes name
                exec(f"self.std_no_{num}.setHidden(False)")
                exec(f"self.std_btn_{num}.setHidden(False)")
                exec(f"self.std_time_{num}.setHidden(False)")
                stdname = name[i-1]
                if len(stdname) == 2:
                    stdname = stdname[0] + '\u3000' + stdname[1] # U+3000 is a FULL-WIDTH SPACE character
                exec(f"self.std_btn_{num}.setText('{stdname}')")
            for i in range(len(name)+1, 31): # Hide absent students
                num = ppint(i)
                exec(f"self.std_no_{num}.setHidden(True)")
                exec(f"self.std_btn_{num}.setHidden(True)")
                exec(f"self.std_time_{num}.setHidden(True)")
            stage = 4

        except FileNotFoundError as e:
            print("[Errno A1] 파일을 선택하지 않았습니다."); print(e)
        except IndexError as e:
            print("[Errno A2] 파일 정보 입력칸에 빈칸이 없는지 확인해 주십시오."); print(e)
        except ValueError as e:
            print("[Errno A3] 형식에 맞게 정보를 입력했는지 확인해 주십시오."); print(e)
        except Exception as e:
            print("[Errno A9] 알 수 없는 오류 발생. 콘솔창을 확인해주세요."); print(f"{e},\n{stage = }")

# Run
if __name__ == '__main__':
    print("프로그램 준비 중...")
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    print("프로그램 준비 완료")
    app.exec_()

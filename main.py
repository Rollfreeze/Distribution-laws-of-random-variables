from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
#pohui

def main():
    Form, Window = uic.loadUiType("qtFiles\qtMain.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()

# точка входа в проект
# не писать ничего снизу этого файла
# разбиваем на другие классы и функции в отдельные файлы
if __name__ == "__main__":
    main()
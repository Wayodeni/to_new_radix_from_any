import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

import scales_of_notation  # Это наш конвертированный файл дизайна
from to_new_radix_from_any import new_radix_from_any as nrfa


class ExampleApp(QtWidgets.QMainWindow, scales_of_notation.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле scales_of_notation.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.getResult.clicked.connect(self.translate)  # Выполнить функцию translate
        # при нажатии кнопки

    def translate(self):
        num = self.inputNum.text()  # Получаем текст из текстового поля inputNum и присваиваем его переменной
        num_radix = self.numRadix.text()
        output_radix = self.outputRadix.text()
        # Изменяем текст в текстовом поле outputNum на тот, который нам дает функция new_radix_from_any
        self.outputNum.setText(str(nrfa(int(num), int(num_radix), int(output_radix))))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()                  # то запускаем функцию main()

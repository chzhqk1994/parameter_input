from PyQt5 import QtWidgets, uic
import sys
import os
import json

default_param = {"dbAddress": "localhost",
                 "dbUser": "user",
                 "dbPasswd": "passwd",
                 "redisAddress": "localhost",
                 "redisUser": "user",
                 "redisPasswd": "passwd"}

actual_param = {}

if not os.path.exists("parameters.json"):
    with open('parameters.json', 'w') as param_file:
        json.dump(default_param, param_file)
        pass
else:
    with open('parameters.json') as param_file:
        actual_param = json.load(param_file)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # call the inherited classes __init__ method
        uic.loadUi('main.ui', self)

        self.set_ui_text(actual_param)

        self.save_bt.clicked.connect(self.save)
        self.reset_bt.clicked.connect(self.reset)

    def set_ui_text(self, dict):
        self.db_ip_text.setText(dict['dbAddress'])
        self.db_user_text.setText(dict['dbUser'])
        self.db_passwd_text.setText(dict['dbPasswd'])
        self.redis_ip_text.setText(dict['redisAddress'])
        self.redis_port_text.setText(dict['redisUser'])
        self.redis_db_name_text.setText(dict['redisPasswd'])

    def save(self):
        actual_param['dbAddress'] = self.db_ip_text.toPlainText()
        actual_param['dbUser'] = self.db_user_text.toPlainText()
        actual_param['dbPasswd'] = self.db_passwd_text.toPlainText()
        actual_param['redisAddress'] = self.redis_ip_text.toPlainText()
        actual_param['redisUser'] = self.redis_port_text.toPlainText()
        actual_param['redisPasswd'] = self.redis_db_name_text.toPlainText()

        with open('parameters.json', 'w') as param_file:
            json.dump(actual_param, param_file)

    def reset(self):
        if not os.path.exists("parameters.json"):
            with open('parameters.json', 'w') as param_file:
                json.dump(default_param, param_file)
        else:
            with open('parameters.json', 'w') as param_file:
                json.dump(default_param, param_file)

        self.set_ui_text(default_param)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
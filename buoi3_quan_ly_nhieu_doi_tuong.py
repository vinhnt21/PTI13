class User:
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.balance = 0


users = []


# show all users
def show_all_users():
    result = ""
    for user in users:
        result += str(user) + "\n"
    return result


# 1. Thêm dữ liệu (dùng append)
def add_user(username, password):
    user = User(username, password)
    # check xem user đã tồn tại chưa
    index = -1
    for i in range(len(users)):
        if users[i].username == username:
            index = i
            break
    if index == -1:
        users.append(user)
        return True
    else:
        return False


print("aaaa")

add_user("admin", "123")
add_user("admin", "123")
add_user("admin1", "123")
a = show_all_users()


# 2. Sửa dữ liệu
def edit_user(username, new_password, new_balance):
    # tìm vị trí của user cần sửa
    index = -1
    for i in range(len(users)):
        if users[i].username == username:
            index = i
            break
    if index != -1:
        users[index].password = new_password
        users[index].balance = new_balance
        return True
    else:
        return False


# 3. Xóa dữ liệu
def delete_user(username):
    # tìm vị trí của user cần xóa
    index = -1
    for i in range(len(users)):
        if users[i].username == username:
            index = i
            break
    if index != -1:
        users.pop(index)
        return True
    else:
        return False


from PyQt6 import uic
from PyQt6.QtWidgets import *


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi3.ui", self)
        users_str = show_all_users()
        self.textBrowser.setText(users_str)
        self.pushButton.clicked.connect(self.add_new_user)

    def add_new_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "" or password == "":
            QMessageBox.warning(self, "Error", "Username or password cannot be empty")
            return
        res = add_user(username, password)
        if res:
            self.textBrowser.setText(show_all_users())
            QMessageBox.information(self, "Success", "Add user successfully")
        else:
            QMessageBox.warning(self, "Error", "User already exists")

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


app = QApplication([])


window = MainApp()
window.show()

app.exec()

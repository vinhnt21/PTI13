from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
from services.GameData import game_data


class GameWindow(QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        uic.loadUi("ui/game.ui", self)
        self.setWindowTitle("Game")
        self.show_game_list()
        self.pushButton.clicked.connect(self.add_game)
        self.pushButton_2.clicked.connect(self.remove_game)

    def show_game_list(self):
        game_list_str = ""
        for game in game_data.game_list:
            game_list_str += f'💚 {game.name}\n'
        self.textBrowser.setPlainText(game_list_str)
        
    def add_game(self):
        # Lấy dữ liệu từ các trường nhập liệu
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        price = float(price)
        game_type = self.lineEdit_3.text()
        description = self.lineEdit_4.text()
        author = self.lineEdit_5.text()
        
        # Add game to the list
        game_data.add_game(name, price, game_type, description, author)
        
        # Cập nhật danh sách game hiển thị, xóa các trường nhập liệu và hiển thị thông báo thành công
        self.show_game_list()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        QMessageBox.information(self, "Success", "Game added successfully!")
    
    
    def remove_game(self):
        name = self.lineEdit.text()
        
        game_data.remove_game(name)
        self.show_game_list()
        self.lineEdit.clear()
        
        QMessageBox.information(self, "Success", "Game removed successfully!")

        
app = QApplication(sys.argv)
window = GameWindow()
window.show()
sys.exit(app.exec())
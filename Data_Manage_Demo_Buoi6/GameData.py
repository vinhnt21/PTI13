from Game import Game
import json

class GameData:
    def __init__(self):
        # Mở file JSON chứa dữ liệu game để đọc
        with open('Data_Manage_Demo_Buoi6/Game.json', 'r') as file:
            self.data = json.load(file)  # Tải dữ liệu từ file JSON vào biến `self.data`
            
        self.game_list = []  # Danh sách chứa các đối tượng Game
        for game in self.data:  # Lặp qua từng game trong dữ liệu JSON
            # Lấy thông tin từng thuộc tính của game
            name = game['name']
            price = game['price']
            type = game['type']
            description = game['description']
            author = game['author']
            # Tạo một đối tượng Game từ dữ liệu
            game_obj = Game(name, price, type, description, author)
            # Thêm đối tượng Game vào danh sách
            self.game_list.append(game_obj)
            
    def add_game(self, name, price, type, description, author):
        # Kiểm tra xem game có tồn tại trong danh sách không
        for game in self.game_list:
            if game.name == name:
                print("Game already exists")  # Thông báo nếu game đã tồn tại
                return
        # Tạo một đối tượng Game mới
        new_game = Game(name, price, type, description, author)
        self.game_list.append(new_game)  # Thêm game mới vào danh sách
        self.data.append(new_game.__dict__)  # Thêm dữ liệu game mới vào danh sách JSON
        # Ghi lại dữ liệu vào file JSON
        with open('Data_Manage_Demo_Buoi6/Game.json', 'w') as file:
            json.dump(self.data, file)
            
    def remove_game(self, name):
        # Tìm và xóa game khỏi danh sách
        for game in self.game_list:
            if game.name == name:
                self.game_list.remove(game)  # Xóa game khỏi danh sách
                break
        # Cập nhật dữ liệu JSON từ danh sách game
        self.data = [game.__dict__ for game in self.game_list]
        # Ghi lại dữ liệu vào file JSON
        with open('Data_Manage_Demo_Buoi6/Game.json', 'w') as file:
            json.dump(self.data, file)
        
    def update_game(self, name, price=None, type=None, description=None, author=None):
        # Tìm game cần cập nhật
        for game in self.game_list:
            if game.name == name:
                # Cập nhật các thuộc tính nếu có giá trị mới
                if price is not None:
                    game.price = price
                if type is not None:
                    game.type = type
                if description is not None:
                    game.description = description
                if author is not None:
                    game.author = author
                break
        # Cập nhật dữ liệu JSON từ danh sách game
        self.data = [game.__dict__ for game in self.game_list]
        # Ghi lại dữ liệu vào file JSON
        with open('Data_Manage_Demo_Buoi6/Game.json', 'w') as file:
            json.dump(self.data, file)
        
# Tạo một đối tượng GameData để quản lý dữ liệu game
game_data = GameData()

# Thêm một game mới
game_data.add_game("Game 1", 50, "Action", "This is a description", "Author 1")

# In danh sách game
for game in game_data.game_list:
    print(game)  # In thông tin từng game trong danh sách
# Cập nhật thông tin game
game_data.update_game("Game 1", price=60, type="Adventure")
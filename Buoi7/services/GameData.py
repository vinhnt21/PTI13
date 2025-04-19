import json
from models.Game import Game  
file_path = 'data/Game.json'

class GameData:
    def __init__(self):
        with open(file_path, 'r') as file:
            self.data = json.load(file)
        print(self.data[0])  
        
        self.game_list = []
        for game in self.data:
            name = game['name']
            price = game['price']
            game_type = game['game_type']  
            description = game['description']
            author = game['author']
            
            game_obj = Game(name, price, game_type, description, author)
            self.game_list.append(game_obj)
    def add_game(self, name, price, game_type, description, author):  # Sửa tên biến
        for game in self.game_list:
            if game.name == name:
                print("Game already exists")
                return
        new_game = Game(name, price, game_type, description, author)
        self.game_list.append(new_game)
        self.data.append(new_game.__dict__)
        with open(file_path, 'w') as file:
            json.dump(self.data, file)
            
    def remove_game(self, name):
        for game in self.game_list:
            if game.name == name:
                self.game_list.remove(game)
                break
        self.data = [game.__dict__ for game in self.game_list]
        with open(file_path, 'w') as file:
            json.dump(self.data, file)
        
    def update_game(self, name, price=None, game_type=None, description=None, author=None):  # Sửa tên biến
        for game in self.game_list:
            if game.name == name:
                if price is not None:
                    game.price = price
                if game_type is not None:
                    game.type = game_type
                if description is not None:
                    game.description = description
                if author is not None:
                    game.author = author
                break
        self.data = [game.__dict__ for game in self.game_list]
        with open(file_path, 'w') as file:
            json.dump(self.data, file)



game_data = GameData()
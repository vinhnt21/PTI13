class Game:
    def __init__(self, name, price, type, description, author, rating):
        self.name = name
        self.price = price
        self.type = type
        self.description = description
        self.author = author
        
    def __str__(self):
        return f"Game: {self.name}, Price: {self.price}, Type: {self.type}, Description: {self.description}, Author: {self.author}"
    
    
    
    

black_wukong = Game("Black Wukong", 100, "Action", "A thrilling action game", "John Doe", 4.5)
red_dead_redemption = Game("Red Dead Redemption", 150, "Adventure", "An epic adventure game", "Jane Doe", 4.8)



import json

with open("buoi6_game.json", "w") as f:
    json.dumps(black_wukong.__dict__,f)
    
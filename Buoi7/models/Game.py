class Game:
    def __init__(self, name, price, game_type, description, author):
        self.name = name
        self.price = price
        self.game_type = game_type
        self.description = description
        self.author = author
        
        
    def __str__(self):
        return f"Game(name={self.name}, price={self.price}, game_type={self.game_type}, description={self.description}, author={self.author})"



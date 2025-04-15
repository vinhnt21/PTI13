class Game:
    def __init__(self, name, price, type, description, author):
        self.name = name
        self.price = price
        self.type = type
        self.description = description
        self.author = author
        
        
    def __str__(self):
        return f"Game(name={self.name}, price={self.price}, type={self.type}, description={self.description}, author={self.author})"
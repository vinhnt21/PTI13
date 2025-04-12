class User:
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.balance = 0



class Word:
    def __init__(self, text, meaning, ipa):
        self.text = text
        self.meaning = meaning
        self.ipa = ipa


class Todo:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.is_done = False

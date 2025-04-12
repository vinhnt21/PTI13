class User:
    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.balance = 0
    def __str__(self):
        return f"Info: {self.username}, {self.password}, {self.balance} "
    def update_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            return True
        else:
            return False
        
        
class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, username, password):
        user = User(username, password)
        # check xem user đã tồn tại chưa
        index = -1
        for i in range(len(self.users)):
            if self.users[i].username == username:  # username bị trùng
                index = i
                break
        if index == -1:  # username không bị trùng
            self.users.append(user)
            return True
        else:
            return False
    def edit_user(self, username, new_password, new_balance):
        # tìm vị trí của user cần sửa
        index = -1
        for i in range(len(self.users)):
            if self.users[i].username == username:
                index = i
                break
        if index != -1:
            self.users[index].password = new_password
            self.users[index].balance = new_balance
            return True
        else:
            return False
    def delete_user(self, username):
        # tìm vị trí của user cần xóa
        index = -1
        for i in range(len(self.users)):
            if self.users[i].username == username:
                index = i
                break
        if index != -1:
            self.users.pop(index)
            return True
        else:
            return False

    def show_all_users(self):
        print("Users::")
        for user in self.users:
            print(user)


user_manager = UserManager()
user_manager.show_all_users()
user_manager.add_user("Duong", "123")
user_manager.show_all_users()
user_manager.add_user("Khanh", "123")
user_manager.show_all_users()
user_manager.delete_user("Duong")
user_manager.show_all_users()

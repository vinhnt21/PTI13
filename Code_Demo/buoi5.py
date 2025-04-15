import json
import os

# Định nghĩa class User
class User:
    def __init__(self, name, password, balance=0):
        self.username = name
        self.password = password
        self.balance = balance

    def to_dict(self):
        """Chuyển đổi đối tượng User thành dictionary để lưu JSON"""
        return {
            "username": self.username,
            "password": self.password,
            "balance": self.balance
        }

# Đọc dữ liệu từ file JSON (nếu có)
def load_users(filename="buoi5_data.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # Đọc danh sách users từ file JSON
            except json.JSONDecodeError:
                return []  # Trả về danh sách rỗng nếu file bị lỗi
    return []  # Trả về danh sách rỗng nếu file chưa tồn tại

# Ghi dữ liệu vào file JSON
def save_users(users, filename="buoi5_data.json"):
    users_dict = [user.to_dict() if isinstance(user, User) else user for user in users]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users_dict, file, indent=4)  # Ghi danh sách users vào file JSON

# Hàm thêm user mới
def add_user(name, password, balance=0):
    users = load_users()  # Load danh sách users
    new_user = User(name, password, balance)  # Tạo user mới
    users.append(new_user.to_dict())  # Thêm user vào danh sách
    save_users(users)  # Lưu lại file JSON
    print(f"✅ Đã thêm user: {name}")


users = load_users()


users.append(User("thai","aaaaaqq"))

save_users(users)
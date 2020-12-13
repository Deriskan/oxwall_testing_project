from datetime import datetime


class User:
    def __init__(self, username="", password="", real_name="", email="", gender=None, birthday=None, is_admin=False):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.gender = gender
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d") if (birthday is not None) else None
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.__class__} object: username={self.username}, real_name={self.real_name}"

    def __repr__(self):
        return f"{self.__class__}(username={self.username}, password={self.password}, real_name={self.real_name})"

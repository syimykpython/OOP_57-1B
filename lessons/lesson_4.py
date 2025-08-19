class User:
    # переменые классы
    total_user = 0

    def __init__(self, name):
        self.name = name
        User.total_user += 1

user_igor = ("igor")
user_kukmanbek = ("kurmanbek")
print(User.total_user)
print(User.get_total_users())
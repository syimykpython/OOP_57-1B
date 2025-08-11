class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Привет меня зовут {self.name}. Я работаю как {self.profession}.")


class Classmate(Person):
    def __init__(self, name, subject):
        super().__init__(name, "студент")
        self.subject = subject

    def introduce(self):
        print(f"привет я {self.name}, твой одногруппник. мы учим {self.subject}.")


class Friend(Person):
    def __init__(self, name, hobby):
        super().__init__(name, "друг")
        self.hobby = hobby

    def introduce(self):

        print(f"эй я {self.name}, твой друг. мне нравится {self.hobby}.")

classmate1 = Classmate('Коля', 'прогрмирования')
classmate2 = Classmate('Мэрим', 'обществознания')

friend1 = Friend('Алан', 'рисования')
friend2 = Friend("Юджин", 'сталкерство')

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

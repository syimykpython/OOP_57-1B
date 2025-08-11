class Person:
    def __init__(self, name, profession, higher_education):
        self.name = name
        self.__profession = profession
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__profession

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu = "у меня есть высшее образование." if self.higher_education else "у меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия — {self.occupation}, {edu}")

class Classmate(Person):
    def __init__(self, name, subject, higher_education):
        super().__init__(name, "студент", higher_education)
        self.subject = subject

    def introduce(self):
        edu = "у меня есть высшее образование." if self.higher_education else "у меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия — {self.occupation}, мы изучаем {self.subject}, {edu}")

class Friend(Person):
    def __init__(self, name, hobby, higher_education):
        super().__init__(name, "друг", higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "у меня есть высшее образование." if self.higher_education else "у меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия — {self.occupation}, моё хобби — {self.hobby}, {edu}")

classmate1 = Classmate('Вектор', 'программирование', True)
classmate2 = Classmate('Тролебузина', 'экономию', True)

friend1 = Friend('Догнатий', 'настолки', False)
friend2 = Friend('Перегнатий', 'чтение', True)

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
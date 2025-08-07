class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation


person1 = Person('Влад', '1999-12-31', 'програмист')
person2 = Person('Даша', '1986-04-26', 'инженер')
person3 = Person('Артем', '1991-12-26', 'врачь')

class Classmate(Person):
    def introduce(self, introduce):
        print(f"higher_education{self.higher_education} is introduce to {introduce}")

class Friend:
    def introduce(self, introduce):
        print(f"have been friends for {self.have_been_friends_for} is introduce to {introduce}")
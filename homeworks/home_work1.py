class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

person1 = Person('Валинтино', '2000-01-01', 'програмист', True)
person2 = Person('Женья', '1986-04-26', 'инженер', True)
person3 = Person('Саша', '1991-12-26', 'врачь', False)

a = [person1, person2, person3]

for person in a:
    print('Имя:', person.name)
    print('Дата рождения:', person.birth_date)
    print('Профессия:', person.occupation)
    print('Высшее образование:', 'Да' if person.higher_education else 'Нет')
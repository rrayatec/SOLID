# _ Nos dice que una clase o función debe centrarse en una única responsabilidad,
# __ que debe existir una única razón para cambiar;
# ___ en resumen podemos decir que éste principio nos pide que todos los métodos
# ____ o sub-funciones tengan alta cohesión.

class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)


if __name__ == '__main__':
    p = Person('John Doe')
    p.save()

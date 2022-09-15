# _ indica que las clases deberían estar abiertas para su extensión,
# __ pero cerradas para su modificación. En otros términos,
# ___ el código debería estar escrito de tal manera que,
# ____ a la hora de añadir nuevas funcionalidades,
# _____ no se deba modificar el código escrito previamente,
# ______ que pueda estar siendo utilizado por otros usuarios.

from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')


class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)

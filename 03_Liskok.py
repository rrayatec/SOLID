# _ Establece que una clase secundaria debe ser sustituible por su clase principal.
# __ El principio de sustitución de Liskov tiene como objetivo garantizar que la
# ___ clase secundaria pueda asumir el lugar de su clase principal sin causar ningún error.

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'send {message} to {email}')


class SMS(Notification):
    def notify(self, _message_, phone):
        print(f'send {_message_} to {phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception(
                'La notificación que nos enviaste no está disponible aun')


if __name__ == '__main__':
    contact = Contact("ruben raya", "rraya@tec.mx", "5514200581")
    not_manager = NotificationManager(SMS(), contact)
    not_manager.send("Hola => ")

from app.typing import T_Name


class Animal:
    def __init__(self, name: T_Name, age: int):
        self.age = age
        self.name = name

    def speak(self):
        return f'Hi! I am {self.name}. I am {self.age} old.'

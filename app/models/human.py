from typing import ClassVar

from app.typing import T_Subjects, T_Name


class Human:
    knowledge: ClassVar[T_Subjects] = []

    def __init__(self, name: T_Name, age: int):
        self.age = age
        self.name = name

        self._phone_number = None
        self.__passport_data = None

    @classmethod
    def from_config(cls, config: dict):
        return cls(**config)

    @staticmethod
    def some_method() -> int:
        return 42

    def speak(self):
        return f'Hi! I am {self.name}. I am {self.age} old.'

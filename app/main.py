import abc

from app.models import Human


class SomeClass(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str:
        ...


def main_function():
    human = Human(name='Vasya', age=12)
    print(human.speak())

    human_2 = Human.from_config(config={'name': 'Petya', 'age': 20})
    print(human_2.speak())

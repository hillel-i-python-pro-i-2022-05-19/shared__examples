import random
from typing import NamedTuple, Iterator, Optional


class Human(NamedTuple):
    name: str
    age: int


class HumanClass:
    def __init__(self, name: Optional[str] = None, age: Optional[int] = None):
        self.age = age or random.randint(18, 90)
        self.name = name or 'Bla'


def generate_human() -> Human:
    # return HumanClass(name='Vasya', age=20)
    return Human(name='Vasya', age=20)


def generate_human2() -> tuple[str, int]:
    return 'Vasya', 20


def generate_human3() -> tuple[int, str]:
    return 20, 'Vasya'


def generator_of_humans_2(amount_of_humans: int):
    for _ in range(amount_of_humans):
        yield generate_human2()


def generate_humans_view_2(amount_of_humans: int) -> str:
    return ''.join(
        f"<p>{human[0]} - {human[1]}</p>" for human in generator_of_humans_2(amount_of_humans=amount_of_humans))


def generator_of_humans(amount_of_humans: int) -> Iterator[Human]:
    # Note: Can make rework with "while" and some structure to ensure uniqueness.
    for _ in range(amount_of_humans):
        yield generate_human()


def generate_humans_view(amount_of_humans: int) -> str:
    return ''.join(
        f"<p>{human.name} - {human.age}</p>" for human in generator_of_humans(amount_of_humans=amount_of_humans))


def main():
    ...


if __name__ == '__main__':
    main()

import hashlib
from typing import TypeAlias, TypedDict, Any


class Item(TypedDict):
    name: str
    age: int
    id: int


T_DB: TypeAlias = list[Item]
T_INDEX: TypeAlias = list[dict[Any, Item]]
T_INDEX__PYTHON: TypeAlias = dict[Any, Item]


def get_data(my_db: T_DB) -> Item:
    for item in my_db:
        if item["id"] == 2:
            return item

    raise KeyError


def create_index(my_db: T_DB, field_name: str) -> T_INDEX:
    # noinspection PyTypedDict
    return sorted(
        ({"key": item[field_name], "value": item} for item in my_db),  # type: ignore
        key=lambda x: x["key"],  # type: ignore
    )


def create_index__python(my_db: T_DB, field_name: str) -> T_INDEX__PYTHON:
    # noinspection PyTypedDict
    return {item[field_name]: item for item in my_db}  # type: ignore


def main():
    my_db: T_DB = [
        {"name": "Aaa", "age": 22, "id": 1},
        {"name": "Bbb", "age": 25, "id": 2},
        {"name": "Ccc", "age": 22, "id": 3},
    ]

    # noinspection PyUnusedLocal
    index__by__id = create_index(my_db=my_db, field_name="id")  # noqa: F841
    # noinspection PyUnusedLocal
    index__by__name = create_index(my_db=my_db, field_name="name")  # noqa: F841

    my_db[1]["age"] = 40

    # noinspection PyUnusedLocal
    index__by__id__python = create_index__python(my_db=my_db, field_name="id")  # noqa: F841
    # noinspection PyUnusedLocal
    index__by__name__python = create_index__python(my_db=my_db, field_name="name")  # noqa: F841

    word = "hello"
    # noinspection PyUnusedLocal
    word_hash = hash(word)  # noqa: F841

    word_hash_2 = hashlib.sha3_512(word.encode())
    # noinspection PyUnusedLocal
    a = word_hash_2.hexdigest()  # noqa: F841

    salt = "bla foo bar"
    word_hash_2.update(salt.encode())
    # noinspection PyUnusedLocal
    b = word_hash_2.hexdigest()  # noqa: F841

    print("Hi")


if __name__ == "__main__":
    main()

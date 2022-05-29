def example_1(arg1: str) -> str:
    return arg1 if arg1 != '' else 'default'


def example_2(arg1: str) -> str:
    return arg1 or 'default'


def main() -> None:
    print(example_1(''))
    print(example_1('value'))

    print(example_2(''))
    print(example_2('value'))


if __name__ == '__main__':
    main()

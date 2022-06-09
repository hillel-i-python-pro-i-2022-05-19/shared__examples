import asyncio
# import multiprocessing
import concurrent.futures
import logging

from init_logging import init_logging


# multiprocessing.Queue()
# lock = multiprocessing.Lock()
# with lock:
#     ...
# multiprocessing.Semaphore()

def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError(f'Incorrect input: {number}')

    elif number == 0:
        return 0

    elif number in {1, 2}:
        return 1

    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_wrapper(number: int) -> int:
    logging.info(f'start {number}')
    result = fibonacci(number=number)
    logging.info(f'end {number}')
    return result


async def fibonacci_async(number: int) -> int:
    if number < 0:
        raise ValueError(f'Incorrect input: {number}')

    elif number == 0:
        return 0

    elif number in {1, 2}:
        return 1

    else:
        return (await fibonacci_async(number - 1)) + (await fibonacci_async(number - 2))


async def fibonacci_wrapper_async(number: int) -> int:
    logging.info(f'start {number}')
    result = await fibonacci_async(number=number)
    logging.info(f'end {number}')
    return result


def calculate_sync(items: list[int]) -> list[int]:
    return list(map(fibonacci_wrapper, items))


def calculate_process(items: list[int]) -> list[int]:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        items_in_generator = worker.map(
            fibonacci_wrapper,
            items,
        )

        items = list(items_in_generator)

        # futures = [
        #     worker.submit(double, number) for number in items
        # ]
        #
        # items = []
        # for future in concurrent.futures.as_completed(futures):
        #     items.append(future.result())

    return items


def calculate_thread(items: list[int]) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor() as worker:
        # results = worker.map(
        #     double,
        #     items,
        # )

        futures = [
            worker.submit(fibonacci_wrapper, number) for number in items
        ]

        items = [future.result() for future in concurrent.futures.as_completed(futures)]

    return items


async def calculate_async(items: list[int]) -> list[int]:
    return await asyncio.gather(*[
        fibonacci_wrapper_async(number) for number in items
    ])


def main():
    items = list(range(32))

    # print(calculate_sync(items=items))
    # print(calculate_process(items=items))
    # print(calculate_thread(items=items))

    # print(asyncio.run(calculate_async(items=items)))

    # logging.info('start')
    # thread = threading.Thread(target=double, args=(10,), daemon=True)
    # thread.start()
    # logging.info('wait')
    # thread.join()
    # logging.info('finish')

    print()


if __name__ == '__main__':
    init_logging()
    main()

from concurrent.futures import ProcessPoolExecutor, TimeoutError
import time
import random


def sleep(number: int) -> int:
    time.sleep(random.randint(number, 20))
    print("Done sleeping")
    return number


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=10) as ex:
        try:
            for result in ex.map(sleep, [1], timeout=2):
                print(result)
        except TimeoutError:
            print("one of the processes failed due to a TimeoutError")

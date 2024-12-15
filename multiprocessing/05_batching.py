from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

def task(number: int) -> int:
    print(f"STARTED TASK {number}")
    return number * 2


if __name__ == "__main__":


    with ProcessPoolExecutor(4) as exe:
        _ = exe.map(task, range(10000), chunksize=500)

    print("All done")

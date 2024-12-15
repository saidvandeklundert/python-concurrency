from concurrent.futures import ThreadPoolExecutor


def task(*args, **kwargs) -> str:
    import time
    time.sleep(5)
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)
    return "done"


if __name__ == "__main__":
    with ThreadPoolExecutor() as ex:
        future = ex.submit(task, 11, 12, 13, d=2)
        print("waiting for the future")
        result = future.result
        
        print(result())
        print("future is in")

 
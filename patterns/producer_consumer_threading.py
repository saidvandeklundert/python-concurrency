import threading
import queue
import time

def producer(q):
    """
    Producer tasks generate items or data and place them on
    the shared buffer.

    The work that is produced needs to be consumed.

    Producers run untill there are no more items to generate.
    
    For instance:
    - retrieve CLI output from network devices
    - interact with servers
    """
    for i in range(5):
        time.sleep(1)
        q.put(f"item {i}")
        print(f"Produced item {i}")

def consumer(q):
    """
    Consumer tasks take or remove items/data from the shared buffer for processing.

    If there are no items in the buffer, the consumer may wait or block.
    
    Consumer tasks may run until there are no further items to consume.
    """    
    while True:
        try:
            item = q.get(timeout=5)  # wait up to 5 seconds for new items
            print(f"Consumed {item}")
            q.task_done()
        except queue.Empty:
            print("No more items to consume")
            break


"""
Thread-safe buffer
"""
q = queue.Queue()

"""
Creating and starting the threads
"""
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

"""
Waiting for the threads to complete:
"""
producer_thread.join()
consumer_thread.join()
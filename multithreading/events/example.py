import threading
import time
import sys

# Create an event object for thread communication
stop_event = threading.Event()

def thread1_function():
    """First thread that waits for 30 seconds and then signals the second thread to stop"""
    try:
        print("Thread 1: Starting, will stop Thread 2 after 30 seconds")
        # Instead of using sleep, use event.wait() which can be interrupted
        if not stop_event.wait(timeout=30):  # Returns False if the wait completed without the event being set
            stop_event.set()  # Signal the second thread to stop
            print("Thread 1: Signaled Thread 2 to stop")
    except Exception as e:
        print(f"Thread 1 error: {e}")
        stop_event.set()

def thread2_function():
    """Second thread that prints 'running' every 5 seconds until signaled to stop"""
    try:
        print("Thread 2: Starting")
        while not stop_event.is_set():
            print("Thread 2: running")
            # Wait for 5 seconds or until the stop event is set
            stop_event.wait(timeout=5)
        print("Thread 2: Stopping")
    except Exception as e:
        print(f"Thread 2 error: {e}")
        stop_event.set()

def main():
    # Create the threads
    thread1 = threading.Thread(target=thread1_function)
    thread2 = threading.Thread(target=thread2_function)

    try:
        # Start both threads
        thread1.start()
        thread2.start()

        # Wait for threads to complete or until interrupted
        while thread1.is_alive() or thread2.is_alive():
            thread1.join(timeout=0.1)
            thread2.join(timeout=0.1)

    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt, stopping threads...")
        stop_event.set()
        
        # Give threads a short time to clean up
        thread1.join(timeout=1)
        thread2.join(timeout=1)
        
        print("Main: Program terminated")
        sys.exit(0)

if __name__ == "__main__":
    main()
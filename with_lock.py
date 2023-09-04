import threading
import time

lock = threading.Lock()


def write_to_file(name, value):
    f = open(name + ".txt", "w")
    f.write(str(value))
    f.close()


def read_file(name):
    f = open(name + ".txt", "r")
    num = f.readline()
    return int(num)


def writer1():
    while True:
        time.sleep(0.5)
        with lock:
            write_to_file('counter1', 40)
            write_to_file('counter2', 60)


def writer2():
    while True:
        time.sleep(0.5)
        with lock:
            write_to_file('counter1', 10)
            write_to_file('counter2', 90)


def reader1():
    while True:
        time.sleep(0.5)
        with lock:
            counter1 = read_file('counter1')
            counter2 = read_file('counter2')
            print(f"Reader 1: Counter1 = {counter1}, Counter2 = {counter2}, Sum = {counter1 + counter2}")


def reader2():
    while True:
        time.sleep(1)
        with lock:
            counter1 = read_file('counter1')
            counter2 = read_file('counter2')
            print(f"Reader 1: Counter1 = {counter1}, Counter2 = {counter2}, Sum = {counter1 + counter2}")


def start():
    # Create and start threads
    writer_thread1 = threading.Thread(target=writer1)
    writer_thread2 = threading.Thread(target=writer2)
    reader_thread1 = threading.Thread(target=reader1)
    reader_thread2 = threading.Thread(target=reader2)

    writer_thread1.start()
    writer_thread2.start()
    reader_thread1.start()
    reader_thread2.start()


if __name__ == '__main__':
    start()

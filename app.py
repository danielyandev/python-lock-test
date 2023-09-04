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


def writer(lock_file=True, sleep_time=1, counter1=50, counter2=50):
    def write():
        write_to_file('counter1', counter1)
        write_to_file('counter2', counter2)

    while True:
        time.sleep(sleep_time)
        if lock_file:
            with lock:
                write()
        else:
            write()


def reader(reader_id, lock_file=True, sleep_time=1):
    def read():
        return read_file('counter1'), read_file('counter2')

    while True:
        time.sleep(sleep_time)
        if lock_file:
            with lock:
                counter1, counter2 = read()
        else:
            counter1, counter2 = read()

        print(f"Reader {reader_id}: Counter1 = {counter1}, Counter2 = {counter2}, Sum = {counter1 + counter2}")


def start(lock_file):
    print('Starting processes with locking files = ' + str(lock_file))
    # Create and start threads
    writer_thread1 = threading.Thread(target=writer, args=(lock_file, 0.5, 40, 60))
    writer_thread2 = threading.Thread(target=writer, args=(lock_file, 0.5, 10, 90))
    reader_thread1 = threading.Thread(target=reader, args=(1, lock_file, 1))
    reader_thread2 = threading.Thread(target=reader, args=(2, lock_file, 0.5))

    writer_thread1.start()
    writer_thread2.start()
    reader_thread1.start()
    reader_thread2.start()

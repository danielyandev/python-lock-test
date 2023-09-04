import os

from dotenv import load_dotenv

from app import start

load_dotenv()


def get_lock_flag():
    return os.getenv('LOCK_FILE') in ['true', 'True', '1']


if __name__ == '__main__':
    lock_file = get_lock_flag()
    start(lock_file)

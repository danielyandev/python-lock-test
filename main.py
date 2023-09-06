import os

from dotenv import load_dotenv

from app import start

load_dotenv()


def get_use_file_lock_flag():
    return os.getenv('USE_FILE_LOCK', 'false').lower() in ['true', '1']


if __name__ == '__main__':
    start(
        get_use_file_lock_flag()
    )

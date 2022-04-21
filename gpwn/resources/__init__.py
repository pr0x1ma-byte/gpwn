import os

def get_path() -> str:
    return os.path.dirname(os.path.abspath(__filename__))


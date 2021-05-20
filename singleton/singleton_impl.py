from typing import Any


class Singleton(type):

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    header: str = None

    def __init__(self, header: str) -> None:
        self.header = header

    def info(self, message):
        print('{} Info: {}'.format(self.header, message))

    def error(self, message):
        print('{} Error: {}'.format(self.header, message))

    def debug(self, message):
        print('{} Debug: {}'.format(self.header, message))

    def log(self, message):
        self.info(message)



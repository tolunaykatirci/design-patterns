from threading import Thread

from singleton.singleton_impl import Singleton, Logger


def push_log(value):
    inside_logger = Logger(value)
    for i in range(10):
        inside_logger.info('pass info')


if __name__ == "__main__":

    process1 = Thread(target=push_log, args=("FOO",))
    process2 = Thread(target=push_log, args=("BAR",))

    process1.start()
    process2.start()

    logger = Logger('LOG')
    logger.error('error message')
    logger.log('log message')


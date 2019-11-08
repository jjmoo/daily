import os
import datetime
import threading


def time_stamp():
    return datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')[:-3]


def thread_name():
    return '[' + threading.current_thread().getName() + ']'


def log(level, tag, msg):
    tag = '<' + tag + '>'
    default_length = 14
    length = len(tag)
    if length < default_length:
        tag += ' ' * (default_length - length)
    lock()
    print(time_stamp(), '', level, '', thread_name(), '\t', tag, '\t', msg)
    unlock()


def d(tag, msg):
    log('D', tag, msg)


def i(tag, msg):
    log('I', tag, msg)


def w(tag, msg):
    log('W', tag, msg)


def e(tag, msg):
    log('E', tag, msg)


def lock():
    print_lock.acquire()


def unlock():
    print_lock.release()


def key_interrupt(name):
    lock()
    e(name, '----------------------------------------')
    e(name, 'KeyboardInterrupt: User Canceled')
    e(name, 'Current work directory: ' + os.path.realpath(os.curdir))
    e(name, '========================================')
    unlock()


print_lock = threading.RLock()

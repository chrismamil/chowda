import os
import itertools


def file_exists(filename):
    return os.path.exists(filename) and os.path.getsize(filename) > 0


def partition(predicate, iterable):
    head = itertools.takewhile(predicate, iterable)
    tail = itertools.dropwhile(predicate, iterable)
    return head, tail

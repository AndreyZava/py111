"""
My little Queue
"""
from typing import Any
import queue

_queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """


    _queue.append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return _queue.pop(0) if _queue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    if len(_queue) > ind:
        return _queue[ind]

def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    _queue.clear()

if __name__ == '__main__':
    ...

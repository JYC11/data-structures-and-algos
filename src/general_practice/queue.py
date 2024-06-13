import threading
from collections import deque
from time import sleep


class Queue:
    def __init__(self):
        self.que = deque()

    def enqueue(self, val):
        self.que.appendleft(val)

    def dequeue(self):
        return self.que.pop()

    def is_empty(self):
        return len(self.que) == 0

    def size(self):
        return len(self.que)


q = Queue()


def place_order(orders):
    for order in orders:
        q.enqueue(order)
        print(order + " placed!")
        sleep(0.5)


def serve_order(orders):
    sleep(1)
    for order in orders:
        print(q.dequeue() + " served!")
        sleep(2)


def placing_and_serving():
    orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def print_binary_with_queue():
    q = Queue()
    nums = [i + 1 for i in range(10)]

    for num in nums:
        q.enqueue(num)

    for i in range(10):
        binary = bin(q.dequeue()).replace("0b", "")
        print(binary)


print_binary_with_queue()

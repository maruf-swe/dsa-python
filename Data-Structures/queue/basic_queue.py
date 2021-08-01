# queue implementation using list
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def display(self):
        return self.queue

    def size_of_queue(self):
        print(len(self.queue))

    def is_empty(self):
        return len(self.queue) == 0


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
print(q1.queue)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
q1.enqueue(5)
q1.enqueue(6)
q1.size_of_queue()
print(q1.is_empty())
print(q1.display())

import queue

q = queue.PriorityQueue()

q.put(5)
q.put(4)
q.put(6)
q.put(2)
q.put(8)
q.put(1)
q.put(9)
print(q.get())
print(q.full())
print(q.get_nowait())

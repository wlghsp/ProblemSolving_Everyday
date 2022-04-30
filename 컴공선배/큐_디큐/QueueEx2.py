


from queue import Queue

q = Queue()

q.put(123)
q.put(456)
q.put(789)


while not q.empty():
    print(q.get())
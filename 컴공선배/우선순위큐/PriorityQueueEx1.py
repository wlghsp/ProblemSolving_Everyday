

from queue import PriorityQueue

pq = PriorityQueue()

pq.put(123)
pq.put(456)
pq.put(789)

while not pq.empty():
    print(pq.get())
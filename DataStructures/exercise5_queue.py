from queue import Queue, LifoQueue, PriorityQueue
from collections import deque
tasks = [
    ("task1", "normal", None),
    ("task2", "critical", 1),
    ("task3", "normal", None),
    ("task4", "critical", 5),
    ("task5", "normal", None),
]
q=Queue()
lq=LifoQueue()
pq=PriorityQueue()
dq=deque()
for task in tasks:
    if task[2]==None:
        q.put(task)
        lq.put(task)
    else:
        pq.put((task[2], task[0], task[1]))
    dq.append(task)

while not q.empty():
    q_=q.get()
    print(q_[0], q_[1])
print()
while not lq.empty():
    lq_=lq.get()
    print(lq_[0], lq_[1])
print()
while not pq.empty():
    pq_=pq.get()
    print(pq_[0], pq_[1], pq_[2])
print()
while dq:
    dq_=dq.popleft()
    print(dq_[0], dq_[1])
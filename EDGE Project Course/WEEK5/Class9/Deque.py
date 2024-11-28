from collections import deque

queue=deque()

queue.append(1)
queue.appendleft(2)
queue.append(3)

print(queue)

print(f"Popped : {queue.popleft()}")
print(queue)

print(f"Popped : {queue.pop()}")
print(queue)
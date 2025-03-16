from collections import deque

print("Initial Queue using deque:")
queue = deque([1, 2, 3, 4, 5])
print(queue)

print("Queue after inserting an element at the end:")
queue.append(6)
print(queue)

print("Queue after deleting the first element:")
queue.popleft()
print(queue)

print("Current size of the queue:", len(queue))

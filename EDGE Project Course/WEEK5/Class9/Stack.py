from collections import deque

stack=deque()

stack.append(10)
stack.append(20)
stack.append(30)
print(f"The Current Stack : {stack}")

print(f"Poping : {stack.pop()}")
print(f"The Stack one pop: {stack}")
print(f"Peak one (last) : {stack[-1]}")
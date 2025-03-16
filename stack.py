print("Initial stack:")
stack = ["a", "b", "c"]
print(stack)

print("Stack after inserting an element:")
stack.append("d")
print(stack)

print("Stack after deleting the top element:")
stack.pop()
print(stack)

print("Current size of the stack:", len(stack))
print("Top element of the stack:", stack[-1])

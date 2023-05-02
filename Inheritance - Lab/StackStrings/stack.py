from typing import List

class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
stack.push("d")
stack.push("e")

print(stack.pop())
print(stack.top())
print(stack.is_empty())
print(stack.__str__())

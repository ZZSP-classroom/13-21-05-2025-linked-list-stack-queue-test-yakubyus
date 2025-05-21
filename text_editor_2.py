class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("No actions to undo")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("No actions to undo")

if __name__ == "__main__":
    stack = Stack()
    stack.push("Typed: Hello")
    stack.push("Typed: World")
    stack.push("Deleted: World")

    print(f"Last Action: {stack.peek()}")
    stack.pop()
    print(f"Last Action: {stack.peek()}")

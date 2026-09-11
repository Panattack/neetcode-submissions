class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not(self.stack):
            self.minStack.append(val)
        else:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

class CustomStack:

    def __init__(self, maxSize: int):
        self.length = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.length:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack :
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        mini = min(k,len(self.stack))
        for i in range(mini):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
class MyStack:
    def __init__(self):
        self.nums = []
        self.size = -1
    
    def push(self, x: int) -> None:
        self.nums.append(x)
        self.size += 1
        
    def pop(self) -> int:
        x = -1
        if not self.empty():
            x = self.nums[self.size]
            self.nums.pop()
            self.size -= 1
        return x
    
    def top(self) -> int:
        return self.nums[self.size]
    
    def empty(self) -> bool:
        return self.size == -1
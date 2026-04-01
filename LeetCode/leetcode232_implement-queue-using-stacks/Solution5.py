class MyQueue:

    def __init__(self):
        self.stk = []
        self.sub_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        if not self.sub_stk:
            while self.stk:
                self.sub_stk.append(self.stk.pop())
        return self.sub_stk.pop()

    def peek(self) -> int:
        if not self.sub_stk:
            while self.stk:
                self.sub_stk.append(self.stk.pop())
        return self.sub_stk[-1]

    def empty(self) -> bool:
        return len(self.stk) == 0 and len(self.sub_stk) == 0 


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # Expected: 1
    print(q.pop())    # Expected: 1
    print(q.empty())  # Expected: False

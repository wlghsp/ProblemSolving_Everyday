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
        return not self.stk and not self.sub_stk


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False
    print(q.pop())    # 2
    print(q.empty())  # True

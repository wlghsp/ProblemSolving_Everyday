class Point:
    def __init__(self, x=0, y= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"



p = Point(1, 2)
s = str(p) # p.__str__() 형식으로 호출함
print(s)   # ㄴ = "(1, 2)"
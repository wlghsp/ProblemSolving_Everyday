import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.nums = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        """Insert val. Returns True if not present, False if already exists."""
        if val in self.dict:
            return False
        else:
            self.dict[val] = self.idx
            self.nums.append(val)
            self.idx += 1
            return True

    def remove(self, val: int) -> bool:
        """Remove val. Returns True if present, False if not exists."""
        if val in self.dict:
            # 핵심 아이디어: 순서를 포기한다.
            # 값의 위치와 마지막 값을 찾는다.
            i = self.dict[val]
            last = self.nums[-1]
            
            # 마지막 위치의 값을 삭제할 대상의 위치에 넣는다
            self.nums[i] = last
            self.dict[last] = i
            
            # 마지막 원소 제거
            self.nums.pop()
            del self.dict[val]
            self.idx -= 1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """Returns a random element. Each element must have equal probability."""
        val = random.choice(self.nums)
        return val


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))   # Expected: True
    print(rs.remove(2))   # Expected: False
    print(rs.insert(2))   # Expected: True
    print(rs.getRandom()) # Expected: 1 or 2
    print(rs.remove(1))   # Expected: True
    print(rs.insert(2))   # Expected: False (already exists)
    print(rs.getRandom()) # Expected: 2

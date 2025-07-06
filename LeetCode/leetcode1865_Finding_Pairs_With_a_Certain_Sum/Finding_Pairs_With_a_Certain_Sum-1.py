from collections import Counter
from typing import List
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
       pass

    def add(self, index: int, val: int) -> None:
        pass

    def count(self, tot: int) -> int:
        pass

if __name__ == "__main__":
    # 예시 입력
    nums1 = [1, 1, 2, 2, 2, 3]
    nums2 = [1, 4, 5, 2, 5, 4]
    obj = FindSumPairs(nums1, nums2)

    # 메서드 호출 예시
    print("count(7):", obj.count(7))   # 예: 8 (정답은 구현에 따라 달라짐)
    obj.add(3, 2)                      # nums2[3] += 2
    print("count(8):", obj.count(8))   # 예: 2
    print("count(4):", obj.count(4))   # 예: 1
    obj.add(0, 1)                      # nums2[0] += 1
    obj.add(1, 1)                      # nums2[1] += 1
    print("count(7):", obj.count(7))   # 예: 11

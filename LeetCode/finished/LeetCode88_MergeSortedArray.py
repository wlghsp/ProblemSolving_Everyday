from typing import List

# 1. 내 풀이
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    j = 0
    for i in range(m, m + len(nums2)):
        nums1[i] = nums2[j]
        j += 1

    nums1 = sorted(nums1)
    print(nums1)

# 1. 정렬
def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
     for i, v in enumerate(nums2):
        nums1[m+i] = v
     nums1[:] = sorted(nums1)
     print(nums1)

# 2. 비교 및 삽입
def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge2(nums1, m, nums2, n) # [1,2,2,3,5,6]
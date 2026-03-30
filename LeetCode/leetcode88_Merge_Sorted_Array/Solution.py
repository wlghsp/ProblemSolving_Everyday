class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2 = m - 1, n - 1
        idx = m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] >= nums2[l2]:
                nums1[idx] = nums1[l1]
                idx -= 1
                l1 -= 1
            else:
                nums1[idx] = nums2[l2]
                idx -= 1
                l2 -= 1

        while l1 >= 0:
            nums1[idx] = nums1[l1]
            l1 -= 1
            idx -= 1
        while l2 >= 0:
            nums1[idx] =  nums2[l2]
            l2 -= 1
            idx -= 1

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test 1: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]

    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print(f"Test 2: {nums1}")  # Expected: [1]

    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    print(f"Test 3: {nums1}")  # Expected: [1]

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stk = []
        for a in asteroids:
            # 충돌이 계속 발생하는 동안 
            # 충돌 조건: 왼쪽에 양수, 오른쪽에 음수
            while stk and stk[-1] > 0 and a < 0:
            # 새행성이 크면 top 삭제 
                if stk[-1] < abs(a):
                    stk.pop()
            # 둘이 같으면 top 삭제 후 break
                elif stk[-1] == abs(a):
                    stk.pop()
                    break
             
                elif stk[-1] > abs(a):
                    break
            else:
                stk.append(a)         
        return stk

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.asteroidCollision([5, 10, -5])
    print(f"Test 1: {result1}")  # Expected: [5, 10]

    # Test case 2
    result2 = solution.asteroidCollision([8, -8])
    print(f"Test 2: {result2}")  # Expected: []

    # Test case 3
    result3 = solution.asteroidCollision([10, 2, -5])
    print(f"Test 3: {result3}")  # Expected: [10]

    # Test case 4
    result4 = solution.asteroidCollision([-2, -1, 1, 2])
    print(f"Test 4: {result4}")  # Expected: [-2, -1, 1, 2]

    # Test case 5
    result5 = solution.asteroidCollision([1, -2, -2, -2])
    print(f"Test 5: {result5}")  # Expected: [-2, -2, -2]

    # Test case 6
    result6 = solution.asteroidCollision([-2, -2, 1,-2])
    print(f"Test 6: {result6}")  # Expected: [-2, -2, -2]
    
    # Test case 7
    result7 = solution.asteroidCollision([-2,2,1,-2])
    print(f"Test 7: {result7}")  # Expected: [-2]
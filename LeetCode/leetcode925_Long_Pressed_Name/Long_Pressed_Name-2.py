class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j < len(typed) and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)



if __name__ == "__main__":
    sol = Solution()
    print(sol.isLongPressedName("alex", "aaleex")) # true
    print(sol.isLongPressedName("saeed", "ssaaedd")) # false

    print(sol.isLongPressedName("xnhtq", "xhhttqq")) # false
    print(sol.isLongPressedName("alex", "aaleexa")) # false

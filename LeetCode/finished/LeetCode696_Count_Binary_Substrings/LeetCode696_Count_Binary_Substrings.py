"""
Give a binary string s,
return the number of non-empty substrings
that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.
"""


def countBinarySubstrings1(s):
    groups = [1]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1

    ans = 0
    for i in range(1, len(groups)):
        ans += min(groups[i-1], groups[i])
    return ans

def countBinarySubstrings(s):
    ans, prev, curr = 0, 0, 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            ans += min(prev, curr)
            prev = curr
            curr = 1
        else:
            curr += 1


    return ans + min(prev, curr)


s = "00110011"
print(countBinarySubstrings(s)) # 6
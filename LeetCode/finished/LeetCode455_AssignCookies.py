
'''
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
'''

# g 그리드 s 는 쿠키
def findContentChildren(g, s):
    g.sort()
    s.sort()

    content, i = 0, 0
    # i는 g 아이들의 욕심 배열을 탐색함.
    for j in range(len(s)):
        if i == len(g):
            break
        if s[j] >= g[i]:
            content += 1
            i += 1

    return content





g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s)) # 1
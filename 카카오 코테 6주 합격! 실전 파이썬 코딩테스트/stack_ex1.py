# 웹브라우저 뒤로가기 기능
my_stack = ["google.com", "github.com", "acimcpc.net", "inflearn.com"]
cur_link = my_stack[-1]
print('스택:', my_stack, '현재 페이지: ', cur_link)

# 유튜브 방문
my_stack.append("youtube.com")
cur_link = my_stack[-1]
print('스택:', my_stack, '현재 페이지: ', cur_link)

# 뒤로 가기
my_stack.pop()
cur_link = my_stack[-1]
print('스택:', my_stack, '현재 페이지: ', cur_link)


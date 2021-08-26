# ()
# (())
# ((()
# True
# True
# False
def open_and_close(sentence: str):  ## sentence = ((()
    # stack에 아무것도 없으면 True
    # stack에 아무것도 없을 때 들어오는 것이 여는 괄호이면 append, 닫는 괄호이면 false 반환
    # 기본적으로 여는 괄호는 append, 닫는 괄호는 pop을 시킨다.
    stack = []
    for door in sentence:
        if len(stack) == 0:
            if door == "(":
                stack.append(door)
            else:
                return False
        elif door == "(":
            stack.append(door)
        elif door == ")":
            stack.pop()
    if len(stack) == 0:
        return True
    return False # 앞에서 true조건에 안 걸렸다면 false (else와 같음 )


str = "(()))"
print(open_and_close(str))

# ()
# (())
# ((()
# True
# True
# False
def open_and_close(sentence: str):  ## sentence = ((()
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
    return False


str = ")))((("
print(open_and_close(str))

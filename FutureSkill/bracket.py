# ()
# (())
# ((()
# True
# True
# False
def open_and_close(sentence: str):  ## sentence = ((()
    if len(sentence) == 0:
        return True
    sen_list = list(sentence)
    top = sen_list[-1]
    bottom = sen_list[0]
    if bottom != top:
        new_sen_list = sen_list[1:-1]
        new_sen = "".join(new_sen_list)
        return open_and_close(new_sen)
    if bottom == top:
        return False

str = "((()"
print(open_and_close(str))

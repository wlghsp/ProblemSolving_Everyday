



# def adder_two(a):
#     a += 2
#
#     return a
#
# b = 2
# c = adder_two(b)
# print(f"b: {b}, c: {c}")

# def append_element(in_list):
#     in_list.append(3)
#
# list_test = [2]
# append_element(list_test)
# print(f"{list_test}") [2,3]

# def append_element(in_list):
#     in_list = [3,4]
#
# list_test = [2]
# append_element(list_test)
# print(f"{list_test}") # [2]

def append_element(in_list):
    in_list[:] = [3,4]

list_test = [2]
append_element(list_test)
print(f"{list_test}") # [2]
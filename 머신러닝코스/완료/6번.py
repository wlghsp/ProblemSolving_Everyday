

nums = [2,3,4,5] # 4, 9, 16, 25
# def sqsum1():
# 	return sum(x**2 if x > 0 for x in nums)

def sqsum2():
  	return sum(x^2 for x in nums if x > 0)

# def sqsum3():
#   	return sum(for x in nums if x > 0 then x^2)

def sqsum4():
  	return sum(x**2 for x in nums if x > 0)

# def sqsum5():
#   	return sum(x^2 if x > 0 for x in nums)

# print(sqsum1())
print(sqsum2())
# print(sqsum3())
print(sqsum4())
# print(sqsum5())

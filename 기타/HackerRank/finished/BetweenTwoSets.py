import math

# Greatest Common Divisor of list


def gcd_list(nums):
    gcd_nums = None
    for i in range(len(nums)):
        if i == 0:
            gcd_nums = nums[i]
        else:
            gcd_nums = math.gcd(gcd_nums, nums[i])
    return gcd_nums

# Least common multiple


def lcm(a, b):
    return int(a * b / math.gcd(a, b))

# least common multiple of list


def lcm_list(nums):
    lcm_nums = None
    for i in range(len(nums)):
        if i == 0:
            lcm_nums = nums[i]
        else:
            lcm_nums = lcm(lcm_nums, nums[i])
    return lcm_nums


def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)

    a_cms = []
    i = 1
    while True:
        temp = lcm_a * i
        if temp > gcd_b:
            break
        a_cms.append(temp)
        i += 1

    answer = 0
    for temp in a_cms:
        is_factor = True
        for bb in b:
            if bb % temp != 0:
                is_factor = False
        if is_factor:
            answer += 1

    return answer


a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))

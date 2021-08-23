"""
A,B에는 
1에서 10까지 들어 올수 있음 

최대 4자리 가능 

"""

nums = input()


if nums[1] == "0":  # a가 10인 경우
    print(10 + int(nums[2:]))  # 2: 으로 하므로 b의 값은 두자리여도 상관 없음
else:  # a가 9이하 1자리인 경우
    print(int(nums[0]) + int(nums[1:]))  # 1: 으로 하므로 b의 값은 두자리여도 상관 없음

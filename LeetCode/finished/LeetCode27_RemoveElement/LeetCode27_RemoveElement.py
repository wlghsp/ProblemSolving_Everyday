
def removeElement(nums, val):
    begin = 0;
    for i in range(len(nums)):
        if nums[i] != val:
            nums[begin] = nums[i]
            begin += 1
    return begin





nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
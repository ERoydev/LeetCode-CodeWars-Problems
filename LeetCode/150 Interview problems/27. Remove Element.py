
def removeElement(nums, val):
    # My solution
    left = 0
    right = len(nums) - 1

    for i in range(len(nums)):
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1

        else:
            left += 1

    return left

print(removeElement([0,1,2,2,3,0,4,2], 2))

def OtherSolution(nums, val):
    # Interesting approach!
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index
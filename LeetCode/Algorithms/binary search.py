def binary_search(numbers, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left = mid_idx + 1

        else:
            right = mid_idx - 1

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 0  1  2  3  4  5  6  7  8  9

nums = [-1,0,3,5,9,12]
print(binary_search(nums, 9))
def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
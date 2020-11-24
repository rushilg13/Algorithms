# Bubble Sort in Python

print("Enter numbers in list (Space seperated):")
nums = list(map(int, input().split()))
for j in range(len(nums)):
    for i in range ((len(nums))-1-j):
        if(nums[i]>nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
print("Sorted array is:")
for i in nums:
    print(i, end=' ')
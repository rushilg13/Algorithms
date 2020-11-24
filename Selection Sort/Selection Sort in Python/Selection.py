# APPROACH - 1

print("Enter numbers in list (Space seperated):")
nums = list(map(int, input().split()))
for i in range(len(nums)):
    mini=min(nums[i:])
    ind=nums.index(mini)
    nums[i], nums[ind] = nums[ind], nums[i]
        
print(nums)
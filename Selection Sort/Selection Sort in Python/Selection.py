# APPROACH - 1

print("Enter numbers in list (Space seperated):")
nums = list(map(int, input().split()))
for i in range(len(nums)):
    mini=min(nums[i:])
    ind=nums.index(mini)
    nums[i], nums[ind] = nums[ind], nums[i]
        
print(nums)



# APPROACH - 2

print("Enter numbers in list (Space seperated):")
A = list(map(int, input().split()))
for i in range(len(A)): 
 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
   
    A[i], A[min_idx] = A[min_idx], A[i] 
  
print ("Sorted array:") 
for i in range(len(A)): 
    print(A[i], end=' ') 

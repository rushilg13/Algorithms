print("Enter numbers in list (Space seperated):")
nums = list(map(int, input().split()))
nums.sort()
print("After sorting the array:")
for i in nums:
    print(i, end=' ')
print("\nEnter number to find:")
k=int(input())
start=0
end=len(nums)
while(start<=end):
    mid = int((start+end)/2)
    if(nums[mid]==k):
        print(k, "Found at index", mid)
        break
    elif(nums[mid]<k):
        start=mid+1
    elif(nums[mid]>k):
        end=mid-1

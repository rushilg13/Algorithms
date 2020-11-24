# Linear search -> O(n)

nums = list(map(int, input().split()))
k = int(input())
flag=1
for i in nums:
    if i==k:
        flag=1
        break
    else:
        flag=0
        
if(flag==1):
    print("Number", k, "found at index", nums.index(k))
else:
    print("Number", k, "is not in the list")

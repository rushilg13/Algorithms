# Merge Sort - Divide And Conquer
def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



print("Enter numbers in list (Space seperated):")
nums = list(map(int, input().split()))
merge(nums)
for i in nums:
    print(i, end=' ')
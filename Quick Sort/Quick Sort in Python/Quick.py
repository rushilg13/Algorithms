# # Quick Sort

# def partition(nums, low, high):
#     i = low - 1
#     pivot = nums[high]
    
#     for j in range(low, high):
#         if nums[j] <= pivot:
#             i = i+1
#             nums[i], nums[j] = nums[j], nums[i]
#     nums[i+1], nums[high] = nums[high], nums[i+1]
#     return(i+1)

# def quicksort(nums, low, high):
#     if len(nums)==1:
#         return nums
#     if low < high:
#         pi = partition(nums, low, high)
#         quicksort(nums, low, pi-1)
#         quicksort(nums, pi+1, high)

# print("Enter numbers in list (Space seperated):")
# nums = list(map(int, input().split()))
# quicksort(nums, 0, len(nums)-1)
# for i in nums:
#     print(i, end=' ')





































# Q1
# find first zeros and remove it.
# list =input()
# for i in range(2,len(list)):
#     print(list[i], end=' ')

#---------------------------------------------------------------------------------------------------
# Q2
# find the first missing positive integer
# def firstMissingPositive(nums):
#     n = len(nums)
#     # 1. Rearrangement Phase
#     for i in range(n):
#         # While loop is key to swap until the correct value is in place
#         while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#             # Correct index for value x is x-1
#             correct_idx = nums[i] - 1
#             nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
#     # 2. Scanning Phase
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
            
#     # 3. If all present
#     return n + 1

# def first_missing_positive(nums):
#     n = len(nums)
    
#     # 1. In-place swap (Cyclic Sort)
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#             j = nums[i] - 1
#             nums[i], nums[j] = nums[j], nums[i]
            
#     print(f"Sorted array: {nums}")
    
#     # 2. Find missing value
#     for i, val in enumerate(nums):
#         if val != i + 1:
#             return i + 1
#     return n + 1

# nums = [3, 4, -1, 1]
# ans = first_missing_positive(nums)
# print(f"Missing value: {ans}") #2

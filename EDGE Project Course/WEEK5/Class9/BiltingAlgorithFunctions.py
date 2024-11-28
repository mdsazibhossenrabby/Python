
# Sorting
nums=[7,3,5,1,5,8]

print(sorted(nums)) # Sort List not in palace
print(nums)
nums.sort() # sort in place
print(nums)

# Searcing

print(3 in nums) # check
print(nums.index(5)) # return index

# Addregation

print(sum(nums))

# Combinatorial Algorithms

from itertools import permutations,combinations

print(list(permutations(nums,2)))
print(list(combinations(nums,2)))
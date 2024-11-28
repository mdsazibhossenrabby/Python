from collections import Counter

nums=[1,2,3,3,4,5,6,6,6,6,9]
count=Counter(nums)
print(count)

print(f"First most common : {count.most_common(1)}")
print(f"2nd most common : {count.most_common(2)}")
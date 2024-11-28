import heapq

nums=[4,1,7,3]
heapq.heapify(nums)
print(nums)

heapq.heappush(nums,2)
print(f"Nums after heap push 2 {nums}")

print(f"First Heap Pop : {heapq.heappop(nums)}")
print(f"Second Heap Pop : {heapq.heappop(nums)}")
print(f"Third Heap Pop : {heapq.heappop(nums)}")
print(nums)


#Without Heappifying

nums1=[4,1,7,3]

print(f"Nums 1 : {nums1}")

print(f"First Heap Pop : {heapq.heappop(nums1)}")
print(f"Second Heap Pop : {heapq.heappop(nums1)}")
print(f"Third Heap Pop : {heapq.heappop(nums1)}")
print(nums1)
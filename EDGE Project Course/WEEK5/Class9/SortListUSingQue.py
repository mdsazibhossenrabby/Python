import heapq

nums=[6,4,2,1,6,8,3,5]
heapq.heapify(nums)

    
SortList=[]

while nums:
    SortList.append(heapq.heappop(nums))
    
print(SortList)
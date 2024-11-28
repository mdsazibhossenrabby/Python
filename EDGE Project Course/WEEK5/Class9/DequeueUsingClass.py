class Dequeue:
    def __init__(self):
        self.arr=[]
        
    def Enque(self,a):
        self.arr.append(a)
        
    def EnqueLeft(self,a):
        self.arr.insert(0,a)
    
    def Deque(self):
        return self.arr.pop()
    
    def DequeLeft(self):
        return self.arr.pop(0)
    
dq=Dequeue()

dq.Enque(10)
print(dq.arr)
dq.Enque(20)
print(dq.arr)
dq.Enque(30)
dq.Enque(40)
print(dq.arr)
dq.EnqueLeft(50)
print(dq.arr)

print(f"Popped : {dq.Deque()}")
print(dq.arr)

print(f"Popped : {dq.Deque()}")
print(dq.arr)

print(f"Popped Left: {dq.DequeLeft()}")
print(dq.arr)
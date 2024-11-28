class Stack:
    def __init__(self):
        self.arr = []
    
    def Push(self, a):
        self.arr.insert(0,a)
    
    
    def Pop(self):
        if not self.IsEmpty():
            return self.arr.pop(0)
        else:
            print("Stack is empty!")
            return None
    
    def Peak(self):
        if not self.IsEmpty():
            return self.arr[0]
        else:
            print("Stack is empty!")
            return None
    
    def IsEmpty(self):
        return len(self.arr) == 0
    
    def Print(self):
        print(self.arr)


sk = Stack()


sk.Push(10)
print(sk.arr)
sk.Push(20)
sk.Push(30)
sk.Push(40)
sk.Push(50)
print(sk.arr)

sk.Print()

print("First element:", sk.Peak())


print("Popped element Now:", sk.Pop())


sk.Print()

print("First element after pop:", sk.Peak())

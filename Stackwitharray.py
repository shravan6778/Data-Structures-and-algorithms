class Stack:
    def __init__(self,size):
        self.li=[]
        self.top=-1
        self.size=size
    def push(self,value):
        if self.isFull():
            print("Stack is full")
        else:
            self.li.append(value)
            self.top+=1
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("The poped element is ",self.li.pop())
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(f"The peeked element is ",self.top)
        
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    def isFull(self):
        if len(self.li)==self.size:
            return True
        return False
    def display(self):
        for i in range(len(self.li)-1,-1,-1):
            print(self.li[i])
stack=Stack(5)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.pop()
stack.peek()
stack.display()
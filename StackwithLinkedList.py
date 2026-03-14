class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
    def push(self,value):
        temp=Node(value)
        if self.top==None:
            self.top=temp
        else:
            temp.next=self.top
            self.top=temp
    def pop(self):
        if self.top==None:
            print("stack is empty")
        else:
            print("pop element is ",self.top.value)
            self.top=self.top.next
    def peek(self):
        print("The peek element is ",self.top.value)
    def display(self):
        temp=self.top
        while temp!=None:
            print(temp.value)
            temp=temp.next
            
stack=Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.pop()
stack.peek()
stack.display()
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # print(f"data-{self.data}, next-{self.next}, self--{self}")

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        

    def createNode(self, data):
        # count=0
        """Standard append function to build the initial list."""
        new_node = Node(data)
        # print(f"new_node={new_node}")
        
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        # print(f"Node{count}new_node_data={new_node.data}, new_node_next={new_node.next}")
        # count+=1
    def insert(self):
        n = int(input("\nEnter an Element to Insert: "))
        temp = Node(n)
        
        print("\nINSERT AS\n1: FIRST NODE\n2: LAST NODE\n3: IN BETWEEN")
        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            temp.next = self.head
            self.head = temp
            if self.last is None: # If list was empty
                self.last = temp
        
        elif ch == 2:
            if self.head is None:
                self.head = temp
                self.last = temp
            else:
                self.last.next = temp
                self.last = temp
        
        elif ch == 3:
            pos = int(input("Enter the Position to Insert: "))
            prev = None
            cur = self.head
            count = 1
            
            while cur is not None and count != pos:
                prev = cur
                cur = cur.next
                count += 1
            
            if count == pos:
                if prev is None: # Inserting at position 1
                    temp.next = self.head
                    self.head = temp
                else:
                    prev.next = temp
                    temp.next = cur
            else:
                print("\nNot Able to Insert")

    def delete(self):
        if self.head is None:
            print("List is Empty. Not Able to Delete")
            return

        print("\nDELETE\n1: FIRST NODE\n2: LAST NODE\n3: IN BETWEEN")
        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            print(f"Deleted Element is {self.head.data}")
            self.head = self.head.next
            if self.head is None:
                self.last = None

        elif ch == 2:
            cur = self.head
            prev = None
            while cur.next is not None:
                prev = cur
                cur = cur.next
            
            print(f"Deleted Element is: {cur.data}")
            if prev is None: # Only one element existed
                self.head = None
                self.last = None
            else:
                prev.next = None
                self.last = prev

        elif ch == 3:
            pos = int(input("Enter the Position of Deletion: "))
            cur = self.head
            prev = None
            count = 1
            while cur is not None and count != pos:
                prev = cur
                cur = cur.next
                count += 1
            
            if cur is not None and count == pos:
                print(f"Deleted Element is: {cur.data}")
                if prev is None: # Deleting head
                    self.head = cur.next
                else:
                    prev.next = cur.next
            else:
                print("Not Able to Delete")

    def search(self):
        if self.head is None:
            print("List is Empty")
            return
            
        value = int(input("Enter the Value to be Searched: "))
        temp = self.head
        pos = 0
        while temp is not None:
            pos += 1
            if temp.data == value:
                print(f"Element {value} is Found at {pos} Position")
                return
            temp = temp.next
        print(f"Element {value} not Found in the List")

    def traverse(self):
        cur = self.head
        if cur is None:
            print("List is empty.")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

# node=Node(10)
# print(node.data)
# print(node.next)

# --- Testing the Code ---
my_list = LinkedList()
my_list.createNode(10)
my_list.createNode(20)
my_list.createNode(30)

print("Current List:")
my_list.traverse()

my_list.insert()
my_list.traverse()

my_list.search()

my_list.delete()
my_list.traverse()
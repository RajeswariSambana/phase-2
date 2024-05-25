class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def search(self,data):
        curr=self.head
        pos=1
        while curr:
            if(curr.data==data):
                print(pos) 
                break    
            else:
                pos+=1
                curr=curr.next

    def delete_begin(self):
        if self.head is None:
            print("no node")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None

    def delete_end(self):
        if self.head is None:
            print("no node")
            #if self.head.next is None:
             #   self.head=None
             #   return delete_end(self)
        else:
            curr=self.head
            while curr.next.next:
                    curr=curr.next
            curr.next=None

    def delete_data(self,data):
        if self.head is None:
            print("no data")
        elif self.head.data==data:
            self.head=self.head.next
        else:
            curr=self.head
            while curr.next and curr.next.data!=data:
                curr=curr.next
            if curr.next is None:
                print("no data")
                return
            curr.next=curr.next.next
                    
    def rev(self):
        if self.head is None:
            print("no data")
        prev=None
        curr=self.head
        next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
        self.display()

    def midvalue(self):
        if self.head is None:
            print("empty")
        else:
            c1=c2=self.head
            while c2.next and c2.next.next:
                c1=c1.next
                c2=c2.next.next
            print(c1.data)

    def minmax(self):
        if self.head is None:
            print("empty")
        else:
            curr=self.head
            minimum=maximum=curr.data
            while curr.next:
                if(curr.next.data>curr.data):
                    maximum=max(maximum,curr.next.data)
                else:
                    minimum=min(minimum,curr.next.data)
                curr=curr.next
                
            print(minimum,maximum)



    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print()

obj=linkedlist()
obj.insert(9)
obj.insert(2)
obj.insert(5)
obj.insert(1)
obj.display()
obj.midvalue()
obj.minmax()








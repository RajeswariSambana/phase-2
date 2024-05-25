class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularlist:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.head.next=newNode
            return
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next           
            newNode.next=self.head
            curr.next=newNode
            self.head=newNode
    
    def insert_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.head.next=newNode
            return
        else:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next           
            newNode.next=self.head
            curr.next=newNode
            # self.head=newNode

    # def delete_begin(self):
    #     if self.head is None:
    #         print("empty")
    #     else:
    #         curr=self.head
    #         while curr.next!=self.head:
    #             curr=curr.next 
    #         self.head=self..next
    #         curr.next=self.head
    def rev(self):
        prev=None
        curr=self.head
        next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
        self.display_forward()


    def display_forward(self):
        if self.head is None:
            print("list is empty")
        print(self.head.data,end="->")
        curr=self.head.next
        while curr!=self.head:
            print(curr.data,end="<->")
            curr=curr.next
        print()

obj=circularlist()
obj.insert_begin(1)
obj.insert_begin(2)
obj.insert_begin(3)
obj.display_forward()
obj.rev()
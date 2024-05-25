class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublelist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_begin(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    
    def insert_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode

    def insert_pos(self,data,pos):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        elif pos==1:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        else:
            curr=self.head
            cnt=0
            while curr:
                cnt+=1
                if cnt==pos-1:
                    newNode.next=curr.next
                    newNode.prev=curr
                    curr.next=newNode
                    newNode.next.prev=newNode
                curr=curr.next
        
    def delete_begin(self):
        if self.head is None:
            print("empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete_end(self):
        if self.head is None:
            print("empty")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

    def delete_data(self,key):
        if self.head.data==key:
            self.head=self.head.next
            self.head.prev=None
        elif self.tail.data==key:
            self.tail=self.tail.prev
            self.tail.next=None
        # else:
        #     self.head=self.head.next                     
        #     while self.head.next:
        #         if self.head.next.data==key:
        #             self.head.next=None

    def delete_pos(self,pos):
        if self.head is None:
            print("empty")
        elif pos==1:
            self.delete_begin()
        else:
            curr=self.head
            cnt=0
            while curr.next:
                cnt+=1
                if cnt==pos:
                    curr.next.prev=curr.prev
                    curr.prev.next=curr.next
                curr=curr.next
            if cnt<pos:
                self.delete_end()


    def display_forward(self):
        if self.head is None:
            print("list is empty")
        curr=self.head
        while curr:
            print(curr.data,end="<->")
            curr=curr.next
        print()

    def display_backward(self):
        if self.head is None:
            print("list is empty")
        curr=self.tail
        while curr:
            print(curr.data,end="<->")
            curr=curr.prev
        print()
        
obj=doublelist()
obj.insert_begin(1)
obj.insert_begin(2)
obj.insert_begin(3)
obj.insert_begin(4)
obj.display_forward()
obj.delete_pos(1)
obj.delete_pos(4)
obj.display_forward()




              



class Node:
    def __init__(self, data=None, next=None):
        self.data = data     # value like 10, 20, etc.
        self.next = next     # link to next node (or None)

class LinkedList:
    def __init__(self):
        self.head = None     # start of the list (None means empty)

    def insert_at_start(self, data):
        node = Node(data, self.head)  # new node points to old head
        self.head = node              # update head to this new node
    def insert_at_end(self,data):
        if(self.head is None):
            self.head = Node(data,None)
        else:
            itr=self.head
            while itr.next:  #loop until itr.next exist
                itr=itr.next
            itr.next=Node(data,None)

    def show(self):
        if self.head is None:
            print("empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end=" --> ")
            itr = itr.next
    
    def datalist(self,data_list):
        
        for data in data_list:
            self.insert_at_start(data)
    
    #for count of linked list
    
    def count(self):
        count = 0
        itr = self.head  # start from head
        while itr:       # loop while itr is not None
            count += 1
            itr = itr.next
        return count
    
    #delete at the respective indices
    def deleteat(self,indices):
        itr=self.head
        if (indices==0):
            self.head=self.head.next
        elif(indices<0 or indices>self.count()):
            print("invalid")
        else:
            count=0
            while(count!=indices-1 and itr.next.next!= None):
                count+=1
                itr=itr.next
            itr.next=itr.next.next
            itr.next=None         #for last elemnt del
        
    #insert at the given indices
    def insert_at_choice(self,indices,data):
        if (indices==0):
            self.insert_at_start(data)
        elif(indices<0 or indices>self.count()):
            print("invalid")
        else:
            count=0
            itr=self.head
            while(count!=indices-1):
                count+=1
                itr=itr.next
            node=Node(data,itr.next)
            itr.next=node
    
    #insert after values found
    def insert_after_value(self,data_after,data_insert):
        itr=self.head
        while(itr is not None):
            if(itr.data==data_after):
                node=Node(data_insert,itr.next)
                itr.next=node
                break
            itr=itr.next

      #remove by value
    def remove_by_value(self,data_to_delete):
        # if list is empty
        if self.head is None:
            return

        # if the node to delete is head node
        if self.head.data == data_to_delete:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next is not None:
            if itr.next.data == data_to_delete:
                itr.next = itr.next.next
                return
            itr = itr.next
               
        

        

ll = LinkedList()         # head = None
ll.datalist(['a','b','c'])
ll.show()                
print("length is",ll.count())
ll.deleteat(2)
# ll.insert_at_choice(2,'aa')
# ll.insert_at_choice(0,'cc')
# ll.insert_after_value('cc','dd')
# ll.remove_by_value('dd')
ll.show()
# head: Always points to the first node of the list. Initially None, updated to the newest node at each insertion.
# data: The value stored in a node (e.g., 10, 20).
# node: A container for data and next (link to the next node).
# next: A pointer to the next node. None means end of the list.
# itr: A temporary pointer used to traverse the list (like an iterator).


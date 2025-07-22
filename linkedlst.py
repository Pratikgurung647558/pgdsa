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
ll = LinkedList()         # head = None
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_start(20)    # head -> 20 -> None
ll.insert_at_start(10)    # head -> 10 -> 20 -> None
ll.show()                 # prints: 10 --> 20 -->

# head: Always points to the first node of the list. Initially None, updated to the newest node at each insertion.
# data: The value stored in a node (e.g., 10, 20).
# node: A container for data and next (link to the next node).
# next: A pointer to the next node. None means end of the list.
# itr: A temporary pointer used to traverse the list (like an iterator).


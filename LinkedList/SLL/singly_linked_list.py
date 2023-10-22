class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.head = node
    
    def insert_after(self, temp, data):
        if temp:
            node = Node(data, temp.next)
            temp.next = node
        
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
        
    def delete_data(self, data):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.data == data:
                self.head = None
        else:
            temp = self.head
            if temp.data == data:
                self.head = temp.next
            else:
                while temp.next is not None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next            

    def search(self,data):
        temp = self.head 
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
        

    def print(self):
        # self.is_empty()
        li = ''
        temp = self.head
        while temp:
            li += '-->' + str(temp.data) 
            temp = temp.next
        return li

    def __iter__(self):
        return SLLIterator(self.head)


class SLLIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data



sll = SinglyLinkedList()
sll.insert_at_start(50)
sll.insert_at_start(10)
sll.insert_at_end(100)
sll.insert_after(sll.search(10), 25)
print(sll.print())
sll.delete_data(25)
sll.insert_at_end(200)
for ele in sll:
    print(ele)



class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next 

                         
class LinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def get_head(self):
        return self.head.data        


    def insert_end(self, data):
        new_node = Node(data, None)
        if self.head.data == None:
            self.head.data = data
        else:
            my_node = self.head
            while my_node.next != None:
                my_node = my_node.next
            my_node.next = new_node

    def display(self):
        my_node = self.head
        print(my_node.data,end=' ')
        while my_node.next != None:
            my_node = my_node.next
            print(f'-> {my_node.data}', end =' ')
        print()

    def length(self):
        new_node = self.head
        if self.head.data == None:
            l = 0
            # print(l)
        else:
            l = 1
            while new_node.next != None:
                new_node = new_node.next
                l += 1
            # print(l)
        return l

    def insert(self, data, index):
        if self.head.data == None:
            self.head.data = data
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            new_node = Node(data, prev_node.next)
            prev_node.next = new_node

    def delete(self, index):
        if index >= self.length():
            raise Exception("Index out of range")
        elif index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head.data = None
        else:
            prev_node = self.head
            for _ in range(index -1):
                prev_node = prev_node.next

            prev_node.next = prev_node.next.next



 
 
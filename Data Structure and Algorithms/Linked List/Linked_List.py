class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next 

                         
class LinkedList:
    def __init__(self):
        self.head = Node(None, None) 


    def insert_end(self, data):
        new_node = Node(data, None)
        if self.head.data == None:
            self.head.data = data
        else:
            my_node = self.head
            while my_node.next != None:
                my_node = my_node.next
            my_node.next = new_node

    def print(self):
        my_node = self.head
        print(my_node.data,end=' ')
        while my_node.next != None:
            my_node = my_node.next
            print(f'-> {my_node.data}', end =' ')
        print()

    def len(self):
        new_node = self.head
        if self.head.data == None:
            print(0)
        else:
            l = 1
            while new_node.next != None:
                new_node = new_node.next
                l += 1
            print(l)

    def insert(self, data, index):
        if self.head.data == None:
            self.head.data = data
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            new_node = Node(data, prev_node.next)
            prev_node.next = new_node

        


    # insert at particular position
    # delete at particular position
 
 
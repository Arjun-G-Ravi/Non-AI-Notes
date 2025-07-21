
class Heap:
    '''This is a binary max heap'''

    def __init__(self, init_arr=None):
        if init_arr:
            self.arr = init_arr
            self.heapify()
        else:
            self.arr = []
        self.len = len(self.arr)

    def get_top(self):
        return self.arr[0] 
    

    def insert(self, i):
        self.arr.append(i)
        curr_index = self.len # the added element will have a zero based index of self.len
        while True:
            parent_index = (curr_index-1)//2
            if parent_index >= 0: # exists
                if i > self.arr[parent_index]:
                    self._swap(curr_index, parent_index)
                    curr_index = parent_index
                    print(i, curr_index)
                    continue
                else:
                    break
            break
            

        self.len += 1

    def remove(self, element):
        pass

    def poll(self):
        '''removing the root node'''
        self.remove(self.arr[0])

    def _swap(self, idx1, idx2):
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]
        
    def show(self):
        print(self.arr)

    def heapify(self):
        pass


if __name__ == "__main__":
    h = Heap()
    h.insert(10)
    h.insert(13)
    h.insert(3)
    h.insert(1)
    h.insert(7)
    h.insert(17)
    h.insert(23)
    h.insert(9)
    h.insert(42)
    h.insert(0)
    h.show()
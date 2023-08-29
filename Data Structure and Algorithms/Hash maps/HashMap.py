class Hash_Map:
    def __init__(self,arr_size=100):
        self.arr_size = arr_size
        self.arr = [[None] for i in range(arr_size)]

    def hash_function(self, key):
        sum_ascii = 0
        for i in key:
            sum_ascii += ord(i)
        return sum_ascii % self.arr_size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if not self.arr[index][0]:
            self.arr[index][0] = (key, value)
        else:
            self.arr[index].append((key, value))
        return True
    
    def get_item(self, key):
        index = self.hash_function(key)
        for i in self.arr[index]:
            if key in i[0]:
                return i[1]  
        raise Exception("Element not found")
                

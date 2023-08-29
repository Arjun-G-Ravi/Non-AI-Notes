class Hash_Map:
    def __init__(self,arr_size=100):
        self.arr_size = arr_size
        self.arr = [[None] for i in range(arr_size)]

    def hash_function(self, key):
        sum_ascii = 0
        for i in key:
            sum_ascii += ord(i)
        return sum_ascii % self.arr_size
    
    def __setitem__(self, key, value):
        index = self.hash_function(key)
        if not self.arr[index][0]: # is None
            self.arr[index][0]=[key, value]
        else:
            for i in self.arr[index]:
                if i[0] == key:
                       i[1] = value
                       return
            self.arr[index].append([key, value])
       
    
    def __getitem__(self, key):
        index = self.hash_function(key)
        for i in self.arr[index]:
            if key in i[0]:
                return i[1]  
        raise Exception("Element not found")
    
    def print_all (self):
        for i in self.arr:
            print(i)
                

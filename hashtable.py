class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) ==  2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

class LPHashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)

    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.add[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
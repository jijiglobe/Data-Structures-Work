class OpenAddressingHashMap:
    class Item:
        def __init__(self,key,value=None):
            self.key = key
            self.value = value
        def __str__(self):
            return "<"+str(self.key)+":"+str(self.value)+">"
        def __repr__(self):
            return str(self)
    def __init__(self):
        self.size = 0
        self.capacity = 3
        self.array = [[]] * self.capacity
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def __getitem__(self,key):
        location = hash(key) % self.capacity
        for item in self.array[location]:
            if item.key == key:
                return item.value
        raise KeyError()
    
    def resize(self,forced = False):
        newarray = None
        if forced or self.size / self.capacity > 0.5:
            newarray = [[]] * (self.capacity * 2)
            self.capacity *=2
        elif self.size / self.capacity < 0.125:
            newarray = [[]] * (self.capacity/2)
            self.capacity = self.capacity //2
        if newarray == None:
            return
        for location in self.array:
            for item in location:
                mapTo = hash(item.key) % self.capacity
                newarray.append(item)
        self.array = newarray

    def __setitem__(self, key, value):
        print(self.array)
        location = hash(key) % self.capacity
        for item in self.array[location]:
            if item.key == key:
                item.value = value
                return
        newItem = OpenAddressingHashMap.Item(key,value)
        self.array[location].append(newItem)
        self.size +=1
        self.resize()

    def __delitem__(self,key):
        location = hash(key) % self.capacity
        for index in range(len(self.array[location])):
            if self.array[location][index].key == key:
                del self.array[location][index]
                return
        self.size -=1
        self.resize()
    def __iter__(self):
        for location in self.array:
            for item in location:
                yield item
    
    def rehash(self):
        self.resize(True)
def test():
    print("adding values...")
    print("adding [1,2,3...20] mapped to strings of themselves")
    test = OpenAddressingHashMap()
    for x in range(1,20):
        test[x] = str(x)
    
test()

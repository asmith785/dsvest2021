class RingBuffer:
    def __init__(self, capacity):
        self.i = 0 #counter for array 
        self.cap = capacity
        self.a = [] #make a empty list
        
    def append(self, item):
        
        # check len of list a if less than capacity append to list
        if len(self.a) < self.cap:
            self.a.append(item)
            print(self.i)
            print(self.a)
        elif self.i == (len(self.a)):
            self.i = 0 
            self.a[self.i] = item
            print(self.i)
            print(self.a)
        else:
            self.a[self.i] = item
            self.i += 1 #add one to the index/counter
            print(self.i)
            print(self.a)

        
    def get(self):
        print(self.a)
        

buffer = RingBuffer(3)
buffer.append(17)
buffer.append(86)
buffer.append(7)
buffer.append(9)
buffer.append(6)
buffer.append(5)
buffer.append(58)
buffer.append(78)
buffer.append(23)
buffer.append(1)

#buffer.get()



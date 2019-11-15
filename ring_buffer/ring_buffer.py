
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else: 
            self.current += 1

    def get(self):
        arr = [i for i in self.storage if i is not None]
        return arr
            

''' for testing
buffer = RingBuffer(5)
print(len(buffer.storage))
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('j')
buffer.append('k')
print(len(buffer.storage))
print(buffer.get())
'''
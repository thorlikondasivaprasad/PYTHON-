class ArrayQueue:
    def __init__(self):
        """Keep track of 3 things"""
        INIT_CAP = 10
        self.data = [None]*INIT_CAP
        self.front = 0
        self.n = 0
    def __len__(self):
        """Return number of elements in queue"""
        return self.n
    def __str__(self):
        return str(self.data)
        #ix_sequence = [(self._front+i)%(len(self._data)) for i in range(self._n)]
        #contents = ",".join([str(self._data[ix]) for ix in ix_sequence])
        #return "[" + contents + "]"
   #####################
   # Note: start with the
   # simple stuff. __getitem__,
   # __len__, __init__, __str__, etc.
    def is_empty(self):
        """Returns true if no elements in queue"""
        return self.n==0

    def dequeue(self):
        """Pop an item from the front of the queue (inch the front pointer along)"""
        if(self.is_empty()):
            raise Empty("oops, empty queue")

        dafront = self.data[self.front]

        self.data[self.front]=None # clean up
        self.front = (self.front+1)%(len(self.data)) # update front pointer
        self.n -= 1
        return dafront
        
    def enqueue(self, e):
        """Add an item to the back of the queue"""
        if(self.n==len(self.data)):
             raise Full("oops, FULL queue")

        insert_index = (self.front + self.n )%(len(self.data))
        self.data[insert_index] = e
        self.n += 1

    def first(self):
        return self.data[self.first]
        
if __name__=="__main__":
    print("Testing ArrayQueue.--1")
    a=ArrayQueue()
    for c in "ABCDEFGHI":
        a.enqueue(c)
        print(a)
    print()
    print("Testing ArrayQueue.--2")
    for i in range(8):
        a.dequeue()
        print(a)

    print()
    print("Testing ArrayQueue.--3")
    for c in "9876543":
        a.enqueue(c)
        print(a)
    print()
    print("Testing ArrayQueue.--4")
    for i in range(6):
        a.dequeue()
        print(a)
    print()
    print("Testing ArrayQueue.--5")
    print("Final:")
    print(a)

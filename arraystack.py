class ArrayStack:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return (len(self.data)==0)

    def push(self,o):
        self.data.append(o)

    def pop(self):
        if(self.is_empty()):
            raise empty("stack is empty")
        return self.data.pop()

    def peek(self):
        if(self.is_empty()):
            raise empty("stack is empty")
        return self.data[-1]

    if __name__=="__main__":
        a = ArrayStack()
        a.push(5)
        a.push(15)
        a.push(17)
        a.push(28)
        print("peeking:{0}".format(a.peek()))
        print("Length of the stack:{0}".format(len(a)))
        a.pop()
        a.pop()
        a.push(100)
        a.push(200)
        a.push(300)
        a.push(400)
        while(not a.is_empty()):
            a.pop()
            print("popping.....:{0}".format(len(a)))
            print("testing arraystack is verified")
        
        

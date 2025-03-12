class MyQueue(object):

    def __init__(self):
        self.arr=[]
        self.top=-1
        self.start=0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        self.top+=1
        # if self.top == 0:
        #     self.start=0
        # return self.arr[self.top]

            
        

    def pop(self):
        """
        :rtype: int
        """
        popped_elem=self.arr[self.start]
        self.start+=1
        return popped_elem

    def peek(self):
        # fifo so peek to first element 
        """
        :rtype: int
        """
        # if self.empty():
        #     raise IndexEror("empty")

        return self.arr[self.start]


    def empty(self):
        """
        :rtype: bool
        """
        return self.start>self.top


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.min_val = []

    def push(self, val):
        if self.min_val:
            if val < self.min_val[-1]:
                self.min_val.append(val)
            else:
                self.min_val.append(self.min_val[-1])
        else:
            self.min_val.append(val)
        return self.min_stack.append(val)

    def pop(self):
        self.min_val.pop()
        return self.min_stack.pop()
        
    def top(self):
        return self.min_stack[-1] if self.min_stack else None
        
    def getMin(self):
        return self.min_val[-1] if self.min_val else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack1(object):

    def __init__(self):
        self.min_stack = []
        self.min_val = []

    def push(self, val):
        self.min_stack.append(val)
        val = min(val, self.min_val[-1] if self.min_val else val)
        self.min_val.append(val)

    def pop(self):
        self.min_val.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.min_stack[-1] if self.min_stack else None
        
    def getMin(self):
        return self.min_val[-1] if self.min_val else None
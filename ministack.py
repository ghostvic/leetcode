'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
#
'''
The main concern here is we'd better get the Min value when insterting numbers, since if not, we have to go through 
the entire list while each getMin().
And, myStack=[] should be put in __init__(self), or there will be some random errors.
'''
#
class MinStack:
        def __init__(self):
            self.myStack = []
        
        # @param x, an integer
        # @return an integer
        def push(self, x):
            curMin = 0
            if len(self.myStack) == 0:
                curMin = x
            elif self.getMin() > x:
                curMin = x
            else:
                curMin = self.getMin()
                
            self.myStack.append((x,curMin))
            return self.myStack[-1][0]
    
        # @return nothing
        def pop(self):
            if len(self.myStack) == 0:
                return None
            
            del self.myStack[-1]
    
        # @return an integer
        def top(self):
            if len(self.myStack) == 0:
                return None
            return self.myStack[-1][0]
    
        # @return an integer
        def getMin(self):
            
            if len(self.myStack) == 0:
                return None
            else:
                return self.myStack[-1][1]

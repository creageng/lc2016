# Design a stack that supports push, pop, top, and retrieving
# the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.minStack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.elements[-1]
        self.elements.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.elements[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
      
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

























class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack=[]
        
        self.min=0
        

    def push(self, val: int) -> None:
        
        if not self.stack:
            self.stack.append(val)
            self.min=val
            
        elif self.min<val:
            
            self.stack.append(val)
        else:
            
            self.stack.append(2*val-self.min)
            
            self.min=val
            
            

    def pop(self) -> None:
        
        if not self.stack:
            return -1
        elif self.stack[-1]<self.min:
            
            self.min=2*self.min-self.stack.pop()
           
        else:
            self.stack.pop()
        
        

    def top(self) -> int:
        
        if not self.stack:
            return -1
        elif self.stack[-1]<self.min:
            
            return self.min
           
        else:
            return self.stack[-1]
        
        
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.min
   
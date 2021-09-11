class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, i: int) -> int:
        
            
        count=1

        while self.stack and self.stack[-1][0]<=i:
            count+=self.stack.pop()[1]


        self.stack.append([i,count])
            
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
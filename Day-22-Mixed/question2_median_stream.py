class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap=[]
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        
        if len(self.max_heap)==len(self.min_heap):
            heappush(self.min_heap,-heappushpop(self.max_heap,-num))
        else:
            heappush(self.max_heap,-heappushpop(self.min_heap,num))
        print(self.min_heap,self.max_heap)

    def findMedian(self) -> float:
        
        if len(self.min_heap)==len(self.max_heap):
            
            return (self.min_heap[0]-self.max_heap[0])/2
        return self.min_heap[0]        


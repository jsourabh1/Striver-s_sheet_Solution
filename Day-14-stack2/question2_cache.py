from collections import OrderedDict
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        
        self.dictt=OrderedDict()
        self.cap=cap
        
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        
        if key not in self.dictt:
            return -1
        self.dictt.move_to_end(key)
        return self.dictt[key]
            
        
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        
        self.dictt[key]=value
        self.dictt.move_to_end(key)
        
        if len(self.dictt)>self.cap:
            self.dictt.popitem(last=False)

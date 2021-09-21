def findSpiral(root):
    # Code here
    
    if not root:
        return []
    ans=[]
    queue=[]
    count=0
    queue.append(root)
    
    while queue:
        
        if count%2==0:
            
            for i in queue[::-1]:
                ans.append(i.data)
            
        else:
            for i in queue:
                ans.append(i.data)
        n=len(queue)
        count+=1
        
        while n:
            
            node=queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            n-=1
            
    return ans
            

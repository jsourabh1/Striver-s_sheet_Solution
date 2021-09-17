def LeftView(root):
    
    if not root:
        return []
    queue=[]
    
    queue.append(root)
    res=[]
    while queue:
        
        res.append(queue[0].data)
        count=len(queue)
        
        while count:
            
            node=queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            count-=1
            
    return res

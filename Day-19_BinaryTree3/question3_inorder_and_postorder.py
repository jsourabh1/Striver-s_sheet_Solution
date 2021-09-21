#Function to return a tree created from postorder and inoreder traversals.
def buildTree(In, post, n):
    
    index=n-1
    
    
    def helper(n,post,start,end):
        nonlocal index
        if start>end:
            return None
            
        node=Node(post[index])
        index-=1
        if start==end:
            return node
            
        # 
        temp=n.index(post[index+1])
        # print(temp)
        
        node.right=helper(n,post,temp+1,end)
        node.left=helper(n,post,start,temp-1)
        return node
    return helper(In,post,0,n-1)
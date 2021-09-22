def LCA(root, p, q):
    #code here.
        if p>q:
            p,q=q,p
            
        def helper(root):
            nonlocal p,q
            
            if not root:
                return None
            
            if  p<root.data and  root.data<q:
                
                return root 
            if p==root.data or q==root.data:
                return root
            if p<root.data and q<root.data:
                return helper(root.left)
            else:
                return helper(root.right)
            
        return helper(root)

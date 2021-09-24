#User function Template for python3
def isBSt(root,maxx,minn):
    
    if not root:
        return True
        
    if root.data<=minn or root.data>=maxx:
        return False
        
    return isBSt(root.left,root.data,minn) and isBSt(root.right,maxx,root.data)
    
def nodes(root):
    
    if not root:
        return 0
        
    return 1+nodes(root.left)+nodes(root.right)
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        #code here
        
        if isBSt(root,float("inf"),-float("inf")):
            
            n=nodes(root)
            # print(n)
            return n
            
        return max(self.largestBst(root.left),self.largestBst(root.right))
            
            
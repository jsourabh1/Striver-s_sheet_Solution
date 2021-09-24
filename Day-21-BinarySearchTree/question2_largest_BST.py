#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, K):
        #your code here
        ans=-1
        count=0
        def solve(root):
            nonlocal K,ans,count
            if not root:
                return -1
                
            if root.right:
                
                solve(root.right)
            # print(count,K)
            count+=1
            if count==K:
                ans=root.data
                
            if root.left:
                
                solve(root.left)
                
            # count+=1
            
            
            
                
            return -1
        solve(root)
        return ans 
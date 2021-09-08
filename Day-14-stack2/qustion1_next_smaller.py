class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        stack=[]
        ans=[-1]*len(A)
        for i in range(len(A)):

            while stack and stack[-1]>=A[i]:
                stack.pop()

            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(A[i])
        return ans

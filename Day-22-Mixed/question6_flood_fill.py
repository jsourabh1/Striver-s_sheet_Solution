# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

#         new=newColor
#         queue=[]
#         queue.append([sr,sc])
#         change=image[sr][sc]

#         if change==new:
#             return image
#         image[sr][sc]=new
#         while queue:

#             first,second=queue.pop(0)


#             if isvalid(image,first+1,second,new,change):
#                 queue.append([first+1,second])
#                 image[first+1][second]=new

#             if isvalid(image,first,second+1,new,change):
#                 queue.append([first,second+1])
#                 image[first][second+1]=new

#             if isvalid(image,first-1,second,new,change):
#                 queue.append([first-1,second])
#                 image[first-1][second]=new

#             if isvalid(image,first,second-1,new,change):
#                 queue.append([first,second-1])
#                 image[first][second-1]=new

#         return image

# def isvalid(image,first,second,new,change):
#     # print(first,second)
#     if first<0 or second<0 or first>=len(image) or second>=len(image[0]) or image[first][second]!=change:
#         return False

#     return True



from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:

        n=len(arr)

        odd=[]
        even=[]

        for i in range(n):

            index=-1

            for j in range(i+1,n):

                if arr[j]>=arr[i]:

                    if index==-1:
                        index=j

                    elif arr[j]<arr[index]:
                        index=j


            odd.append(index)
            index=-1
            for j in range(i,n):

                if arr[j]<=arr[i]:

                    if index==-1:
                        index=j

                    elif arr[j]>arr[index]:
                        index=j

            even.append(index)

        count=0
        print(even,odd)

        #         for i in range(n):

        #             j=i
        #             jump=1

        #             while j<n:

        #                 if jump%2==0:

        #                     if even[j]==-1:
        #                         break

        #                     j=even[j]

        #                 else:

        #                     if odd[j]==-1:
        #                         break

        #                     j=odd[j]

        #                 jump+=1

        #             if j==n-1:
        #                 count+=1


        return count


obj=Solution()

obj.oddEvenJumps([[10, 13, 12, 14, 15]])

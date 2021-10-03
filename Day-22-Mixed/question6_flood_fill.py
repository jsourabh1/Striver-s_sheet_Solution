class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        new=newColor
        queue=[]
        queue.append([sr,sc])
        change=image[sr][sc]

        if change==new:
            return image
        image[sr][sc]=new
        while queue:

            first,second=queue.pop(0)


            if isvalid(image,first+1,second,new,change):
                queue.append([first+1,second])
                image[first+1][second]=new

            if isvalid(image,first,second+1,new,change):
                queue.append([first,second+1])
                image[first][second+1]=new

            if isvalid(image,first-1,second,new,change):
                queue.append([first-1,second])
                image[first-1][second]=new

            if isvalid(image,first,second-1,new,change):
                queue.append([first,second-1])
                image[first][second-1]=new

        return image

def isvalid(image,first,second,new,change):
    # print(first,second)
    if first<0 or second<0 or first>=len(image) or second>=len(image[0]) or image[first][second]!=change:
        return False

    return True



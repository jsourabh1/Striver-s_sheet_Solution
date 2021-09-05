from typing import List


def isSafe(row,col,m,n,visited):

    if (row >=0 and row < n and 
        col >=0 and col <n and 
        visited[row][col]==False and m[row][col] == 1):
        return True

    return False


def printPathUtil(row,col,m,n,path,possiblePaths,visited):

    
    if (row == n - 1 and col == n - 1):
        possiblePaths.append(path)
        return

    # Mark the cell as visited
    visited[row][col] = True

 
    # Check if downward move is valid
    if (isSafe(row + 1, col, m, n, visited)):
        path += 'D'
        printPathUtil(row + 1, col, m, n, 
                      path, possiblePaths, visited)
        path = path[:-1]

    # Check if the left move is valid
    if (isSafe(row, col - 1, m, n, visited)):
        path += 'L'
        printPathUtil(row, col - 1, m, n, 
                      path, possiblePaths, visited)
        path = path[:-1]

    # Check if the right move is valid
    if (isSafe(row, col + 1, m, n, visited)):
        path += 'R'
        printPathUtil(row, col + 1, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

    # Check if the upper move is valid
    if (isSafe(row - 1, col, m, n, visited)):
        path += 'U'
        printPathUtil(row - 1, col, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

   
    visited[row][col] = False
class Solution:


    def findPath(self,m: List[List[int]], n: int) -> None:
    
        # vector to store all the possible paths
        possiblePaths = []
        path = ""
        visited = [[False for _ in range(5)]
                          for _ in range(n)]
                          
        
        printPathUtil(0, 0, m, n, path, 
                      possiblePaths, visited)
        return possiblePaths


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()

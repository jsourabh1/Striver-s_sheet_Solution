#User function Template for python3
def empty(arr):
    
    for i in range(9):
        
        for j in range(9):
            
            if arr[i][j]==0:
                return i,j,True
    return 0,0,False
    
def okay_col(first,second,grid,num):
    
    for i in range(9):
        
        if grid[first][i]==num:
            return False
            
    return True
    
def okay_row(first,second,grid,num):
    
    for i in range(9):
        
        if grid[i][second]==num:
            return False
            
    return True
    
def okay_box(first,second,grid,num):
    
    for i in range(3):
        
        for j in range(3):
        
            if grid[i+first][j+second]==num:
                return False
            
    return True
    
    
class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        
        first,second,ans=empty(grid)
        
        if not ans:
            return True
            
        
        for i in range(1,10):
            
            if okay_row(first,second,grid,i) and okay_col(first,second,grid,i) and okay_box(first-first%3,second-second%3,grid,i):
                
                grid[first][second]=i
                
                
                if self.SolveSudou(grid):
                    return True
                    
            grid[first][second]=0
            
        return False
        
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        
        for i in range(9):
            
            for j in range(9):
                
                print(arr[i][j],end=" ")
            print()
                
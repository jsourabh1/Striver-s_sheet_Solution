def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    
    stack1.append(x)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if stack1:
            stack2=[]
            while stack1:
                temp=stack1.pop()
                stack2.append(temp)
            temp=stack2.pop()
            while stack2:
                stack1.append(stack2.pop())
            return temp
    return -1
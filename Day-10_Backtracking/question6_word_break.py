#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this funct
    
    def solve(line,dictt,string2,start):
        
        if start==len(line):
            
            return True
        word=""
        for i in range(start,len(line)):
            
            word+=line[i]
            # print(word)
            if word in dictt :
                
                if solve(line,dictt,string2+" "+word,i+1):
                    return True
                    
    return solve(line,dictionary,"",0)
    
    
    
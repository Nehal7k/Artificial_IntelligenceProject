import math
class Information2:
    temp=1
    Size_of_Tree=0
class player:
    def __init__(self,let):
        self.let=let
        if let=='x':
            
            self.com='x'
            self.player='o'
        else:
            self.com='o'
            self.player='x'
        
    treeSize=0
    def minimaxi(self,borad,depth,ismax=True):
  
        score=borad.evale()

        if score !=None :
            return score,depth
        
     
        scores=[]
        
        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                    if ismax:
                        
                        borad.borad[y][x]=self.com
                    else:
                        borad.borad[y][x]=self.player
                    Information2.temp+=1 
                    s,d=self.minimaxi(borad,depth+1,not ismax)
                    
                    depth=d
                    scores.append(s)
                    borad.borad[y][x]=''
                    
        return (max(scores) if ismax else min(scores)),depth
    def best_move(self,borad):
        depthcount=0
        scores=[]
       # depths=[]
        points=[]
        for y in range(3):
            for x in range(3):
                if borad.borad[y][x]=='':
                    
                    borad.borad[y][x]=self.com
                    Information2.temp+=1 
                    s,d=self.minimaxi(borad,1,False)
                    scores.append(s)
                    depthcount+=1
                  #  depths.append(d)
                    points.append((x,y))
                    borad.borad[y][x]=''
        return (scores,points,depthcount)

   

   
               
            
        
        
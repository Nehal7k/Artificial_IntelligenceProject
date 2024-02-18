from borad import borad
from player import player, player
from player2 import player as player2
from player import Information
from player2 import Information2
import math
import time


sizeTree=0
c='o'
p='x'
human=player(p)
com=player(c)
com2=player2(c)

bord = borad(c,p)
0
bord.show()

maxtime1=0.0
maxtime2=0.0
print('player='+p+'  computer='+c)
while 1:
 
  
    x=input('inter x : ')
    y=input('inter y : ')
    
    w=bord.change(human,(int(x),int(y)))
    if w is not None:
        if w==1:
            print('computer won')
        elif w==-1:
        
            print('player won')

        elif w==2:
            continue
        else:
            print('tie')

        break
    
    start1=time.time()            
    (s,pp,dd)=com.best_move(bord)
    Information.Size_of_Tree+=Information.temp
    endwin1=time.time()
    maxtime1+= endwin1 - start1

    Maxdepth1=com.best_move(bord)

    start2=time.time()
    (s2,pp2,dd2)=com2.best_move(bord)
    Information2.Size_of_Tree+=Information2.temp
    endwin2=time.time()
    maxtime2+=endwin2-start2
    big_score=-1000

    index=0
    for i in range(len(s)):
         if s[i]>big_score:
            big_score=s[i]
            index=i
            
    print('\n\n')
    print('__________________________________________')
    print('depth minimax without alpha betta :')
    print(dd2)
    print('__________________________________________')
    print('depth minimax  with alpha betta :')
    print(dd)
    print('__________________________________________')
    
            
            
               
   
    w=bord.change(com,(pp[index][0],pp[index][1]))
    bord.show()
    if w is not None:
        if w==1:
            print('computer won')
           



        elif w==-1:
        
            print('player won')

        else:
            print('tie')

        break

print('the time in alphabeta is     : ',str(maxtime1))
print('the time in minmax is :',str(maxtime2))
print('\n')
ass1=Information()
print("Size of tree in AlphaBeta : ")
print(ass1.Size_of_Tree)
ass2=Information2()
print("Size of tree in minmax : ")
print(ass2.Size_of_Tree)






  

                
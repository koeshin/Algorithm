import sys


R,C=map(int,sys.stdin.readline().split())

grid=[]

min_pos= (0,0)
min_num=10**6
for i in range(R):
    tmp=list(map(int,sys.stdin.readline().split()))
    for j in range(C):
        
        if tmp[j]< min_num:
            min_num=tmp[j]
            min_pos=(i,j)
    grid.append(tmp)



def go_right(p1,p2,C):
    
    a=p1
    b=p2

    for i in range(C-1):
        b=b+1
        print('R',end='')
    
    return a,b

def go_left(p1,p2,C):
    a=p1
    b=p2

    for i in range(C-1):
        b=b-1
        print('L',end='')
    
    return a,b

def go_down(p1,p2,R):
    a=p1
    b=p2

    for i in range(R-1):
        a=a+1
        print("D",end='')
    
    return a,b

def go_up(p1,p2,R):
    a=p1
    b=p2

    for i in range(R-1):
        a=a-1
        print('U',end='')
    
    return a,b



def sol1(): ## R=홀수
    
  
    rep=C-1
    for i in range(R):
        if i%2==0:
            if i!=R-1:
                print('R'*rep+'D',end='')
            else:
                print('R'*rep)
                
        else:
            print('L'*rep+'D',end='')

        

    return 

def sol2(): ## C=홀수
    
    rep=R-1
    for i in range(C):
        if i%2==0:
            if i!=C-1:
                print('D'*rep+'R',end='')
            else:
                print('D'*rep)
                
        else:
            print('U'*rep+'D',end='')

    return 

def  sol3():
    min_p1=min_pos[0]
    min_p2=min_pos[1]
    min_range=min_p1//2


    
    for i in range(R//2):
        if i<min_range:
            print('R'*(C-1)+'D',end='')
            
            print('L'*(C-1)+'D',end='')
            
        elif i == min_range:
           
            for j in range(0,C-1):
                
                if j<min_p2:
                    
                    if j%2==0:
                        if min_p2==0:
                            print('R',end="")
                        print('DR',end="")
                    else:
                        if j!=C-1:
                            print('UR',end="")
                        else:
                            print('URD',end="")
                            
                else:
                    if j%2==0 :
                        print('RD',end="")
                    else:
                        print('RU',end="")
        else:
            print('L'*(C-1)+'D',end='')
            
            if i!=R//2-1:
                print('R'*(C-1)+'D',end='')
            else:
                print('R'*(C-1),end='')
                
    
    return

def sol():
    if R%2!=0:
        sol1()
    elif C%2 !=0:
        sol2()
    else:
        sol3()
    return  

sol()



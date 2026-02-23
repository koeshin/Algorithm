import sys


N,M=map(int,sys.stdin.readline().split())

miro=[]

for _ in range(M):
    tmp=sys.stdin.readline().strip()
    tmp_list=[]
    for str in tmp:
        tmp_list.append(int(str))
        
    miro.append(tmp_list)

visited=[[False]*N for _ in range (M)]

global res
res=10**10

def DFS(now,door):
    global res
    move=[(1,0),(0,1),(-1,0),(0,-1)]
    x,y=now
    if door> res:
        return
    if x==M-1 and y==N-1:
        res=min(res,door)
        return
    for mx,my in move:
        tx=x+mx
        ty=y+my
        
        if 0<= tx<M and 0<=ty <N:
            if visited[tx][ty] is False:
                visited[tx][ty]=True
                if miro[tx][ty]=='1':
                    DFS((tx,ty),door+1)
                else:
                    DFS((tx,ty),door)
                visited[tx][ty]=False
    return


  

def BFS():
    global res
    move=[(1,0),(0,1),(-1,0),(0,-1)]
    start=(0,0)
    
    qq=[start]
    visited[0][0]=True
    while(qq):
        now=qq.pop(0)
        x,y=now
        for mx,my in move:
            tx=x+mx
            ty=y+my
            if 0<= tx<M and 0<=ty <N:
                if visited[tx][ty] is False:
                    visited[tx][ty]=True
                    if miro[tx][ty]==1:
                        miro[tx][ty]=miro[x][y]+1
                        qq.append((tx,ty))
                    else:
                        miro[tx][ty]=miro[x][y]
                        qq.insert(0,(tx,ty))
    return

BFS()    
                 
print(miro[M-1][N-1])
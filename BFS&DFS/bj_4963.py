import sys


gp=[]



def make_gp(w,h):
    
    if w==0 and h==0:
        return 0
    gp=[]
    for i in range(h):
        tmp=list(map(int,sys.stdin.readline().split()))
        gp.append(tmp)
    return gp

def find_land(gp,w,h):
    visited=[[False]*w for _ in range(h)]

    cnt=0
    bfs_list=[]
    dr=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    for i in range(h):
        for j in range(w):
            if gp[i][j]==1 and visited[i][j] is False:
                bfs_list.append((i,j))
                visited[i][j]=True
                while(bfs_list):
                    ty,tx=bfs_list.pop(0)
                    for dy,dx in dr:
                        mx=tx+dx
                        my=ty+dy
                        
                        if 0<= mx<w and 0<=my<h:
                            if gp[my][mx]==1 and visited[my][mx] is False:
                                visited[my][mx]=True
                                bfs_list.append((my,mx))

                cnt+=1
    return cnt
                        
                        
                        
                    


while(True):
    w,h=list(map(int,sys.stdin.readline().split()))
    gp=make_gp(w,h)
    # print(gp)
    if gp==0:
        break
    else:
        cnt=find_land(gp,w,h)
        print(cnt)
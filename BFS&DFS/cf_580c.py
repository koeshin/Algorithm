import sys
sys.setrecursionlimit(10000000)
n,m=map(int,sys.stdin.readline().split())

cats=list(map(int,sys.stdin.readline().split()))
cats=[0]+cats
T= [ [] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    T[a].append(b)
    T[b].append(a)
    
global res
res=0
def dfs(v,cnt):
    global res
    flag=cats[v]
    visited[v]=True
    
    if flag==1:
        cnt=cnt+1
    else:
        cnt=0
        
    # print('v:',v)
    # print('ctn:',cnt)
    
    if cnt>m:
        return
    
    v_cnt=0
    
    for k in T[v]:
        if visited[k] is False:
            v_cnt+=1
            dfs(k,cnt) 
            visited[k]=False
            
    if v_cnt==0:
        res+=1
    return


def fast_sol(v,parent,cnt):
    global res
    
    flag=cats[v]
 
    if flag==1:
        cnt=cnt+1
    else:
        cnt=0
        

    
    if cnt>m:
        return
    
    
    is_leaf=True
    for k in T[v]:
        if k!=parent:
            is_leaf=False
            fast_sol(k,v,cnt)
    if is_leaf and v!=1:
        res+=1
        return
     


fast_sol(1,0,0)
print(res) 
    
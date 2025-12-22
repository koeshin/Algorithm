import sys
sys.setrecursionlimit(10000000)
V=int(sys.stdin.readline())



graph=[ []*V for _ in range(V)]

for i in range(V):
    tmp=list(map(int,sys.stdin.readline().split()))

    for j in range(1,len(tmp),2):
        
        num=tmp[j]
        if num == -1:
            break
        else:
            v=tmp[j] -1
            length=tmp[j+1]
            
            graph[i].append((v,length))
    
global res
res=0
def DFS(point,visited):
    global res
    visited[point]=True
    child_length=[]
    # print('point',point)
    for v,length in (graph[point]):
        # print('v:',v)
        if visited[v] is False :
            child=DFS(v,visited)
            # print('child:',child)
            child_length.append(child+length)
    
    # print('child_length:',child_length)
    if len(child_length)>0:
        child_length.sort(reverse=True)
        if len(child_length)>1:
            check=child_length[0]+child_length[1]
            res=max(res,check)
        else:
            res=max(res,child_length[0])
        return child_length[0]
    else:
        return 0
  
    
visited=[False]*V

DFS(0,visited)
print(res)
    
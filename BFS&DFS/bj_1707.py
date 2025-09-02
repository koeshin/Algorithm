import sys
sys.setrecursionlimit(1000000)
k=int(sys.stdin.readline())

cases=[]
for i in range(k):
    V,E=list(map(int,sys.stdin.readline().strip().split()))
    
    tmp=[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a,b=list(map(int,sys.stdin.readline().strip().split()))
        tmp[a][b]=1
        tmp[b][a]=1
    
    cases.append(tmp)
        
        
def solution(start,graph,visited):
    global check
    
    qq=[]
    color=0
    visited[start]=color
    qq.append(start)
    # print('start:',start)
    
    while(qq):
        if check is False:
            break
        tmp=qq.pop(0)
        for i in range(1,len(graph[tmp])):


            if graph[tmp][i]==1:
                if visited[i]==-1:
                    qq.append(i)
                    color=1-color
                    visited[i]=color
                    # print('i:',i)
                elif visited[i]==visited[tmp]:
                    # print('i,start:',i,tmp)
                    # print('ddd')
                    check=False
                    return
    return


for i in range(k):
    graph= cases[i]

    global check
    check=True
    
    visited=[-1]*len(graph[0])
    
    for j in range(1,len(visited)):
        if visited[j]==-1:
            solution(j,graph,visited)


    if check is True:
        print('YES')
    else:
        print('NO')
    
    



import sys


N = int(sys.stdin.readline())

citys=[]

for _ in range(N):
    tmp=list(map(int,sys.stdin.readline().strip().split()))
    citys.append(tmp)

global res
res=float('inf')

def dfs(start,cur,visited,cost,depth):
    global res
    

    if cost>res: # 가지치기
        return
    
    if depth==N-1:
        if citys[cur][start]!=0:
            cost+=citys[cur][start]
            if res>cost:
                res=cost

    for i in range(N):
        if i!=start and visited[i] == 0 and citys[cur][i]!=0:
            visited[i]=1
            dfs(start,i,visited,cost+citys[cur][i],depth+1)
            visited[i]=0  ## gpt가 알려줌



def solution(tsp):

    for start in range(N):
        visited=[0]*N
        visited[start] = 1  ## gpt가 알려줌
        dfs(start,start,visited,0,0)
    return

solution(citys)
print(res)

    
import  sys


# 너무 어렵다 ....

    

def dfs(remain,n):
    
    global result
    
    if remain==N//2:    # 남은 인원이 4명이 떄 이부분을 생각 못 함...
        start,link=0,0  # 스타트 팀과 링크팀
        for i in range(N):
            for j in range(N):
                if visited[i]and visited[j]:  # 둘 다 방문 했으면 스타트 팀
                    start+= maps[i][j]
                elif not visited[i] and not visited[j]: # 둘 다 방문 X -> 링크팀 
                    link+= maps[i][j]
        
        result=min(result,abs(start-link))   # 최솟값 
        return

    else:
        for x in range(n,N):   #  n 이상 멤버들 고르기
            if visited[x]==0:  # 고르지 않았을 경우에만 
                visited[x]=1   # 방문 처리
                dfs(remain+1,x+1) # 재귀 남은 인원, n 값 늘려주기
                visited[x]=0    # 백트레킹 
                
                
N= int(sys.stdin.readline())
maps=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[0]*N

result=float('inf')                
dfs(0,0)
print(result)
    
    

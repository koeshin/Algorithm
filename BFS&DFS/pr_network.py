from collections import deque

# 네트워크에 대해 이해하지 못 했음. 네트워크는 하나의 길로 연결 연결되는 것. 어떤 컴퓨터와도 연결되지 않으면 자기자신과 연결 +1, 이런 경우. 약간 요격 미사일과 비슷한 방식으로 N개의 컴퓨터를 몇개에 꼬치에 나누어 끼느냐 같은 문제에서는 DFS를 실행한 횟수가 답이 된다.
def dfs(input,idx,computers):
    global visited
    global answer
    
    
    for i in range(len(input)):
        if input[i]==1 and visited[i]==0:
            visited[i]=1   

            dfs(computers[i],i,computers)
    
def solution(n, computers):
    global visited
    visited=[0]*n 
    global answer
    answer = 0
    
    for i in range(len(computers)):
        if visited[i]==0:
            visited[i]=1            
            dfs(computers[i],i,computers)
            answer+=1


    return answer
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

import sys

N,M,start=map(int,(sys.stdin.readline().split()))

graph=[[False]*(N) for i in range(N)]
visited=[False]*N

for _ in range(M):
    a,b=map(int,(sys.stdin.readline().split()))

    graph[a-1][b-1]=True
    graph[b-1][a-1]=True

# print(graph)
dfs_res=[start]
def DFS(graph,start):
        
    # print(visited)
    visited[start]=True
    print(start+1,end=' ')
    for i in range(len(graph[start])):
        if graph[start][i]==True and visited[i]==False :
                DFS(graph,i)
            
    return

DFS(graph,start-1)
print()
# print(dfs_res)

bfs_res=[start]

def bfs(graph,start):
    que=[start]
    visited[start]=True
    while que:
        tmp=que.pop(0)
        print(tmp+1,end=' ')
        for i in range(len(graph[tmp])):
           if graph[tmp][i]==True and visited[i]==False:
            #    print(i)
                que.append(i)
                visited[i]=True

               


visited=[False]*N
bfs(graph,start-1)


# for i in range(len(dfs_res)):
#     print(dfs_res[i],end=' ')
# print()
# for i in range(len(bfs_res)):
#     print(bfs_res[i],end=' ')
# print(bfs_res)

                

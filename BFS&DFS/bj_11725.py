import sys
sys.setrecursionlimit(10**6) ## recursion error 
N=int(sys.stdin.readline())

tree= [[] for _ in range(N+1)]

parent=[0]*(N+1)

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())

    ## 양방향 트리 생성
    tree[a].append(b)  
    tree[b].append(a)

def dfs(node):
    for neig in tree[node]: # 현재 노드와 연결된 이웃노드들 방문
        if parent[neig] ==0: # 부모가 없으면 현재 노드를 이웃 노드의 부모로 설정
            parent[neig]=node
            dfs(neig) # dfs니까 자식 노드타고 들어가서 리프까지 가야함.
            
dfs(1)

for i in range(2,N+1):
    print(parent[i])
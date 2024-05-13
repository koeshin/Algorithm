import sys


N,M=map(int,(sys.stdin.readline().split()))
# print(N,M)

stack=[]  # 답을 담을 리스트
visited=[False]*(N+1)  # 방문 처리를 위한 리스트
def dfs ():
    
    if len(stack)==M:    # 리스트의 개수가 M일 때 탈출 
        print(' '.join(map(str,stack)))
        return
    for i in range(1,N+1):
        if visited[i] ==False:
            stack.append(i)
            # print(stack)
            visited[i] = True
            dfs()
            stack.pop()
            visited[i] = False
            
            
            
dfs()
'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''


'''import sys
from collections import deque
N,K=list(map(int,sys.stdin.readline().split()))

    
visited=[0]*(100001)    

def bfs(V,K):
    
    
    
    
    # print(visited)
    tmp=deque()    
    tmp.append(V)
    # print("tmp: ",tmp)
    visited[V]=1
    while(tmp):
        curr=tmp.popleft()
        
        if curr==K:
            # return visited[K]-1
            print(visited[K]-1)
            
        # print("curr:",curr) 

        if curr<K:
            curr1=curr+1
            if  visited[curr1]==0: 
                visited[curr1]=visited[curr]+1
                tmp.append(curr1)
        if 2*curr<=2*K:
            curr2=curr*2
            if  visited[curr2]==0: 
                visited[curr2]=visited[curr]+1
                tmp.append(curr2)
        if 1<=curr:
            curr3=curr-1
            # print("curr3:",curr3)
            if  visited[curr3]==0: 
                visited[curr3]=visited[curr]+1
                # print("visited:",visited[curr3])
                tmp.append(curr3)
            
    return


bfs(N,K)
'''

import sys
from collections import deque

def bfs2(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = list(map(int,sys.stdin.readline().split()))
array = [0] * MAX
res2=bfs2(n)

# for i in range(100000):
#     for j in range(100000):
#         N,K = i,j
#         n, k = N,K
#         array = [0] * MAX
#         res2=bfs2(n)
#         res=bfs(N,K)
        
#         if res != res2:
#             print("eror")
#             print("i,j:",i,j)
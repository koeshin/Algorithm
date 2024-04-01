'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

'''

import sys

N,M=map(int,(sys.stdin.readline().split()))


graph=[]
visited=[[False]*M for _ in range(N) ]
cnt_graph=[[1]*M for _ in range(N) ]


for i in range(N):
    tmp=(str(sys.stdin.readline().strip()))
    # print(tmp)
    list=[]
    for j in range(len(tmp)):
        list.append(int(tmp[j]))
    # print(list)
    graph.append(list)

#상,하,좌,우
dx=[0,0,-1,1]
dy=[1,-1,0,0]


def bfs(start):

    x,y=start[0],start[1]
    
    
    visited[x][y]==True
    queue=[start]
    while(queue):
        start=queue.pop(0)
        x=start[0]
        y=start[1]
        
        if x==N-1 and y==M-1:
            print(cnt_graph[N-1][M-1])
            break
        for i in range(len(dx)):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            
            
            if 0<=tmp_y<M and  0<=tmp_x<N :
                if graph[x][y]==1 and visited[tmp_x][tmp_y]==False:
                    # print(tmp_x,tmp_y)
                    visited[tmp_x][tmp_y]=True
                    cnt_graph[tmp_x][tmp_y]=cnt_graph[x][y]+1
                    queue.append((tmp_x,tmp_y))

bfs((0,0))

# print(cnt_graph)
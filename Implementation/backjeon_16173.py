'''문제
‘쩰리’는 점프하는 것을 좋아하는 젤리다. 단순히 점프하는 것에 지루함을 느낀 ‘쩰리’는 새로운 점프 게임을 해보고 싶어 한다. 새로운 점프 게임의 조건은 다음과 같다.

‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.
새로운 게임이 맘에 든 ‘쩰리’는, 계속 게임을 진행해 마침내 최종 단계에 도달했다. 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지, 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다. ‘쩰리’는 유능한 프로그래머인 당신에게 주어진 구역에서 승리할 수 있는 지 알아봐 달라고 부탁했다. ‘쩰리’를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!

입력
입력의 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.

입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.

게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

출력
‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.'''

import sys



size=int(sys.stdin.readline().strip())

map_of_games=[]

for i in range(size):
    tmp=list(map(int,sys.stdin.readline().split()))
    map_of_games.append(tmp)


#아래, 오른 순서
dx=[0,1]
dy=[1,0]
start=[1,1]
end=[size,size]
# 0번 인덱스는 아래 이동 1번 인덱스는 오른쪽 이동
# move_1=[] # 첫 이동 시 아래 이동 위치
# move_2=[] # 찻 이동시 오른쪽 이동 위치

# #처음 움직임
# steps=map_of_games[0][0]
# move_1=[start[0]+steps*dy[0],start[1]]
# move_2=[start[0],start[1]+steps*dx[1]]


#업데이트를 위한 위치를 담는 리스트 move_1의 아래 오른쪽 move_2의 아래 오른쪽 순으로 리스트에 담음
# 만약 업데이트가 필요 없다면 None으로 대체
update=[[1,1]]

# update 길이가 1일 떄는 for 문에 작동 안함

while(update):
        # print(update)
        
            # 각 움직인 자리에 스텝 검사
        tmp=update.pop(0)
        # print("tmp",tmp)
        update_step=[0,0]
        # 현재 자리에 step 검사
        # print("tmp[0]",tmp[0])
        # print("tmp[1]",tmp[1])
        steps=map_of_games[tmp[0]-1][tmp[1]-1]
        # if tmp[0]+steps>size and tmp[1]+steps>size:
        #     del update[0]
        #     continue
        
        if tmp[0]+steps<=size and tmp[1]+steps<=size: #둘 다 업데이트
            update_step=[tmp[0]+dy[1],tmp[1]+steps*dx[1]]
            if update_step==[size,size]:
                print("HaruHaru")
                sys.exit()
            update.append(update_step)
            update_step=[tmp[0]+dy[0],tmp[1]+steps*dx[0]]
            update.append(update_step)

        elif tmp[0]+steps<=size and tmp[1]+steps>size: #아래 업데이트
            update_step=[tmp[0]+dy[0],tmp[1]+steps*dx[0]]
            update.append(update_step)

        elif tmp[0]+steps>size and tmp[1]+steps<=size: # 오른쪽 업데이트
            update_step=[tmp[0]+dy[1],tmp[1]+steps*dx[1]]
            update.append(update_step)
            
        if update_step==[size,size]:
            print("HaruHaru")
            sys.exit()
            # del update[0]

print("Hing")


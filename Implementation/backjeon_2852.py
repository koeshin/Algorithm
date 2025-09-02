

import sys
def format_time(seconds):
    return "{:02d}:{:02d} ".format(seconds // 60, seconds % 60)




N=int(sys.stdin.readline().strip())

# 이긴 시간을 저장하는 리스트 0번이 1팅, 1번이 2팀
win_time=[0,0]
max_time=48*60
stack=[]
win_team=None

for i in range(N):
    tmp_list=sys.stdin.readline().split()
    time_list=tmp_list[1].split(":")
    tmp_time=(int(time_list[0])*60)+int(time_list[1]) # 초로 변환

    if len(stack)==0:
        win_team=tmp_list[0]
        stack.append(tmp_time)
    elif win_team==tmp_list[0]:
        stack.append(tmp_time)
    elif win_team!= tmp_list[0]:
        pop_time=stack.pop()
        if len(stack)==0:
            if tmp_list[0]=="1":
                win_time[1]=win_time[1]+(tmp_time-pop_time)
            else:
                win_time[0]=win_time[0]+(tmp_time-pop_time)


if len(stack)>0:
    if win_team=='1':
        win_time[0]=win_time[0]+(max_time-stack[0])
    elif win_team=='2':
        win_time[1]=win_time[1]+(max_time-stack[0])

for _ in win_time:
    
    res=format_time(_)
    print(res)
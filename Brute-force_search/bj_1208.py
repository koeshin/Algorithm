import sys

global cnt
cnt=0

N,S=list(map(int,sys.stdin.readline().split()))

numbers=sys.stdin.readline().strip().split()

up_num=[]
down_num=[]

for num in numbers:
    if int(num)>=0:
        up_num.append(int(num))
    else:
        down_num.append(int(num))

up_num.sort(reverse=True)
down_num.sort(reverse=True)



def solution(up_idx,down_idx,sum_):
    global cnt

    print('sum:',sum_) 
    if up_idx> len(up_num)-1 or down_idx>len(down_num)-1:
        return
    if sum_>=S: # 현재 sum_이 음수니까 양수를 뽑아라
        cur=up_num[up_idx]
    
    else: # 현재 sum_이 양수니까 음수를 뽑아라
        cur=down_num[down_idx]
        
    sum_+=cur
    if sum_ ==S:
        cnt+=1
   
    if sum_>=S:
        if abs(down_num[-1])>=sum_-S:
            solution(up_idx,down_idx+1,sum_)
    elif sum_<S:
        if up_num[-1]>=S-abs(sum_):
            solution(up_idx+1,down_idx,sum_)
    
    if cur>=0:
        solution(up_idx+1,down_idx,sum_-cur)
    elif cur<0:
        solution(up_idx,down_idx+1,sum_-cur)
    return

solution(0,0,0)
print(cnt)
    

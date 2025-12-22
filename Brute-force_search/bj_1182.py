import sys

global cnt
cnt=0

N,S=list(map(int,sys.stdin.readline().split()))

numbers=list(map(int,sys.stdin.readline().strip().split()))


def solution(idx,sum_):
    global cnt
    if idx==N:
        return
    
    sum_+=numbers[idx] ## 이걸 먼저 해야 0일 때, 바로 정답 처리 방지 가능
    if sum_==S:
        cnt+=1

    solution(idx+1,sum_)
    solution(idx+1,sum_-numbers[idx])



solution(0,0)

print(cnt)
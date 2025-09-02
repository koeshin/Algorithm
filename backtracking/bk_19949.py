import sys

# global correct
# correct=list(map(int,sys.stdin.readline().strip().split()))

# global answer
# answer=0

def dfs(depth):
    global cnt
    if depth == 10:
        s = 0
        for j in range(10): # 맞은 정답 개수 확인
            if li[j] == ans[j]:
                s += 1
        if s >= 5:   # 5개 이상이면 탈출
            cnt += 1
        return 
    for i in range(1, 6):
        if depth > 1 and li[depth-2] == li[depth-1] == i: # 찍은 개 2개 이상, 연속 3개가 같은 경우  컨티뉴
            continue
        li.append(i)
        dfs(depth+1)
        li.pop()
        
ans = list(map(int, input().split()))
li, cnt = [], 0
dfs(0)
print(cnt)
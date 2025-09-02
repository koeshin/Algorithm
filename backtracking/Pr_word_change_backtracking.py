

# 프로그래머스 단어 변화 백트래킹으로 풀기
def check_diff(begin,target):
    res=0
    for i in range(len(begin)):
        if begin[i]!=target[i]:
            res+=1
    return res

global answer
answer=50
global visited
visited=[False]*50
def dfs(start,target,words,step):
    # print(start)
    global answer,visited
    if answer<= step:      # 백트래킹 탈출. 현재 스탭이 정답보다 크면 돌아오기
        return              
    if start==target:
        answer=min(answer,step)  # 정받은 항상 최솟값으로 유지
        return answer
    for i in range(len(words)):
        if check_diff(start,words[i]) !=1 :  
            continue

        if visited[i]==False:
            visited[i]=True
            dfs(words[i],target,words,step+1)

            visited[i]=False
            
     
    return       


def solution(begin,target,words):
    global answer
    dfs(begin,target,words,0)

    if answer==50:
        return 0 
    return answer
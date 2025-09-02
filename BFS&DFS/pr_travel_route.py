

def dfs(start,tickets,course,visited,idx): # 현재위치, 티켓 리스트, 지금까지 코스, 방문기록, 이전에 사용한 티켓의 인덱스 입력
    global answer
    curr=start    # 현재 위치
    course_copy=course.copy()  # 이동경로 복사
    visited_copy=visited.copy() # 방문 기록 복사
    course_copy.append(curr)    # 이동경로에 현재 위치 추가

    if len(course_copy)==len(tickets)+1:   # 총 이동한 도시는 티켓 수 +1 => 모든 곳을 다 갔으면 리터
        answer.append(course_copy)
        
        return 
    
    for i in range(len(tickets)):
        if tickets[i][0]==curr and visited_copy[i]==0:  # 티켓의 출발지가 현재 위치이고 사용안한 티켓일 때,
            visited_copy[i]=1    #  방문 처리
            dfs(tickets[i][1],tickets,course_copy,visited_copy,i) # 재귀 dfs
        if i==len(tickets)-1:   # 만약 티켓의 마지막 인덱스까지 갔지만 이동하지 못하고 갇히는 경우
            visited[idx]=0      # 이전에 사용한 티켓의 방문하지 않음으로 수정 -> 갇히면 다른 경우의 수 고려
    return 
def solution(tickets):
    global answer
    answer = []
    v=[0]*len(tickets)   # 사용한 티켓을 저장하는 리스트 
    for i in range(len(tickets)):
        course=["ICN"]          # 시작은 무조건 인천
        visited=v.copy()
        if tickets[i][0]=="ICN":  # 출발지가 인천인 곳 찾기
            visited[i]=1          # 티켓 사용으로 처리
            dfs(tickets[i][1],tickets,course,visited,i) # dfs
    answer.sort()
    answer=answer[0]
    return answer
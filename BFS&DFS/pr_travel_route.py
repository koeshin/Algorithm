

def dfs(start,tickets,course,visited,idx):
    global answer
    curr=start
    course_copy=course.copy()
    visited_copy=visited.copy()
    course_copy.append(curr)

    if len(course_copy)==len(tickets)+1:
        answer.append(course_copy)
        
        return 
    
    for i in range(len(tickets)):
        if tickets[i][0]==curr and visited_copy[i]==0:
            visited_copy[i]=1
            dfs(tickets[i][1],tickets,course_copy,visited_copy,i)
        if i==len(tickets)-1:
            visited[idx]=0
    return 
def solution(tickets):
    global answer
    answer = []
    v=[0]*len(tickets)
    for i in range(len(tickets)):
        course=["ICN"]
        visited=v.copy()
        if tickets[i][0]=="ICN":
            visited[i]=1
            dfs(tickets[i][1],tickets,course,visited,i)
    answer.sort()
    answer=answer[0]
    return answer
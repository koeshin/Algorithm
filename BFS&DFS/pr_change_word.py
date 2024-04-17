
def check_diff(begin,word): # 현재 단어와 다른 단어의 개수 리턴
    res=0
    for i in range(len(begin)):
        if begin[i]!=word[i]:
            res+=1
    return res

def dfs(begin, target, words,visited):
    global l
    res=0
    visited_tmp=visited.copy()   # visited 복사
    visited_tmp[words.index(begin)]=1  # words리스트에서 현재 단어의 인덱스 가져와서 방문 처리
    if begin==target: # 현재 단어가 타겟하고 같으면 이동 횟수 리턴

        res=sum(visited_tmp)  # 총 이동 횟수 계산
        l.append(res)
        
    for i in range(len(words)):
    
        if visited_tmp[i]==0:   # 방문하지 않은  단어 이고
            check_res=check_diff(begin,words[i])
            if check_res==1:    # 다른 글자 수가 한개이면 dfs
                dfs(words[i],target,words,visited_tmp)
                
    return   
def solution(begin, target, words):
    answer = 0
    global l
    l=[]
    if target not in words:   # target 단어가 words에 없을 경우, 리턴
        answer=0
        return answer
    for i in range(len(words)):   
        visited=[0]*len(words)   # 방문한 단어 리스트
        
        check_res=check_diff(begin,words[i]) # 다른 글자 수 확인
        if check_res==1:  #1글자만 다르면 dfs
            
            dfs(words[i],target,words,visited)
            
    answer=min(l)
    return answer

def check_diff(begin,word):
    res=0
    for i in range(len(begin)):
        if begin[i]!=word[i]:
            res+=1
    return res

def dfs(begin, target, words,visited):
    global l
    res=0
    visited_tmp=visited.copy()
    visited_tmp[words.index(begin)]=1 
    if begin==target:

        res=sum(visited_tmp)
        l.append(res)
        
    for i in range(len(words)):
    
        if visited_tmp[i]==0:
            check_res=check_diff(begin,words[i])
            if check_res==1:
                dfs(words[i],target,words,visited_tmp)
                
    return   
def solution(begin, target, words):
    answer = 0
    global l
    l=[]
    if target not in words:
        answer=0
        return answer
    for i in range(len(words)):
        visited=[0]*len(words)
        
        check_res=check_diff(begin,words[i])
        if check_res==1:
            print(words[i])
            dfs(words[i],target,words,visited)
            
    answer=min(l)
    return answer
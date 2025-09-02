import sys

# 지피티가 아이디어 줌 개천재야 지피티
N= int(sys.stdin.readline().strip())


stack=[]
cnt=0


def safe(row,col,col_check,diag,back_diag):  # 컬럼, 대각선, 역대각선 에 대해 안전한지 확인하는 함수
    if col_check[col]==True or diag[col-row+(N-1)]==True or back_diag[col+row]==True:
        return False
    return True


def dfs(depth,col_check,diag,back_diag):
    global cnt,stack
    if len(stack)==N:  # 퀸의 개수가 N개일 때 탈출
        cnt+=1
    
        return
    for i in range(N):
        s=safe(depth,i,col_check,diag,back_diag) # 현재 위치가 안전한 자리인지 확인.
        if s ==True:
            stack.append([depth,i])
            col_check[i]=True         # 컬럼 확인 리스트
            diag[i-depth+(N-1)]=True  # 대각선 확인 리스트 (인덱스: col-row 값이 작은 것 부터 순서대로)
            back_diag[depth+i]=True   # 역대각선 확인 리스트 (인덱스: col+row 값의 합으로 인덱스)
            dfs(depth+1,col_check,diag,back_diag)  # 재귀 

            ########### 백트레킹##########
            stack.pop()                 
            col_check[i]=False 
            diag[i-depth+(N-1)]=False
            back_diag[depth+i]=False
            ##############################

def solution(N):
    
    col_check=[False]*N
    diag=[False]*(2*N-1)
    back_diag=[False]*(2*N-1)    
    
    dfs(0,col_check,diag,back_diag)
    

solution(N)
print(cnt)
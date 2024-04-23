import sys


N=int(sys.stdin.readline().strip())

arr=[]
for i in range(N):
    tmp=list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)
    
def get_subarray(arr, i, j, m):  # numpy를 못 써서 지피티가 작성한 코드
    # i*m과 j*m은 시작점이며, i*m+m과 j*m+m은 각각의 차원에서 끝점을 나타냅니다.
    # 리스트 컴프리헨션을 사용하여 각 행을 슬라이스 하고, 그 결과를 다시 리스트로 만듭니다.
    return [row[j*m:j*m+m] for row in arr[i*m:i*m+m]]

def check_paper(window):  # 종이 안에 숫자들이 다 같은지 확인하는 함수
    n=len(window)
    
    check_num=window[0][0]

    for i in range(n):
        for j in range(n):
            if window[i][j]!=check_num:
                return False  # 숫자가 다르면 리턴
    return True

result=[0,0,0] #-1,0,1, 종이의 개수를 담음
def solution(arr,N,result):
    
    window=arr
    if check_paper(window)==True:   # 숫자가 전부 같으면 종이 숫자에 따라 결과값 +1
        if window[0][0]==-1:
            result[0]+=1
        elif window[0][0]==0:
            result[1]+=1
        else:
            result[2]+=1
        return 
    else:
        m=N//3  # 종이를 9등분
        l=N//m  # 큰 종이를 잘랐을 때 나오는 종이의 개수 여기서는 디폴트 9임.
        for i in range(l):
            for j in range(l):
                window=get_subarray(arr,i,j,m)
                # print("wind",window)
                solution(window,m,result)

solution(arr,N,result)
for i in result:
    print(i)
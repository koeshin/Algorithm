import sys


N=int(sys.stdin.readline().strip())

arr=[]

for i in range(N):
    tmp=list(sys.stdin.readline().strip())
    arr.append(tmp)
print(arr)

def check_sector(arr):   # 구역의 값이 모두 같은지 확인하는 코드
    m=len(arr)

    if m==1:
        return True
    
    a=arr[0][0]
    b=arr[0][1]
    if a!=b: 
        return False
    else:
        for i in range(m):
            for j in range(0,m,2):
                if a!=arr[i][j] or a!=arr[i][j+1]:
                    return False
    
    return True



def get_subarray(arr, i, j, m):  # numpy를 못 써서 지피티가 작성한 코드
    # i*m과 j*m은 시작점이며, i*m+m과 j*m+m은 각각의 차원에서 끝점을 나타냅니다.
    # 리스트 컴프리헨션을 사용하여 각 행을 슬라이스 하고, 그 결과를 다시 리스트로 만듭니다.
    return [row[j*m:j*m+m] for row in arr[i*m:i*m+m]]



global ans
ans=''

def solution(arr,N):
    global ans
    res=check_sector(arr)
    if res==True:
        ans=ans+arr[0][0]  # check_sector==True일 경우 ans에 값 추가

        return
    else:
        ans=ans+'('  # 새로운 섹터가 시작되면 ( 추가
        m=N//2
        l=N//m
        for i in range(l):
            for j in range(l):
                window=get_subarray(arr,i,j,m)
                # print("window",window)
                solution(window,m)
            
        ans=ans+')'   #한 구역이 끝나면 ) 추가
        

solution(arr,N)
print(ans)
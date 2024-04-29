

def solution(triangle):

    
    
    for i in range(len(triangle)-2,-1,-1): # 삼각형은 위에서 두 번째부터 시작
        for j in range(len(triangle[i])):
            tmp=max(triangle[i+1][j],triangle[i+1][j+1])  # 이전 단계에서 맥스값 찾기
            triangle[i][j]=triangle[i][j]+tmp #현재 단계 값 업데이트 
    
    return triangle[0][0]
            



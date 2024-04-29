
import sys

N=int(sys.stdin.readline().strip())
list=[]
for i in range(N):
    tmp=int(sys.stdin.readline().strip())
    list.append(tmp)

def solution(num):
    global answer
    # print("num: ", num)
    num_list=[]
    

    if len(num)==0:
        return
    for k in num: 
        for i in range(3):   # 리스트 안에 들어있는 값을 3,2,1로 뺌
            if k-(i+1)>0:    # 뺀 값이 0보다 크면 num_list에 담음 
                num_list.append(k-(i+1))
                if k-(i+1)<=3: # 뺀 값이 3보다 작으면 이 떄부턴 정답이므로 answer +1
                    answer +=1
            
    return  solution(num_list)
# solution([10])
# print("answer:",answer)


for num in list:
    global answer
    answer=0
    if num<=3:   # 들어가는 숫자 값이 3보다 작으면 answer의 기본값을 1로. 이 부분을 생각 못 함.
        answer=1
        
    
    solution([num])
    print(answer)
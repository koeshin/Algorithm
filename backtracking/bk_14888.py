import sys


N= int(sys.stdin.readline().strip())

numbers=list(map(int,sys.stdin.readline().split()))

oper_num=list(map(int,sys.stdin.readline().split()))




global max,min
oper_list=[]
max=-10**10
min=10**10

def div(num1,num2):
    if num1<0:
        result=-(abs(num1)//num2)
        return result
    
    return num1//num2
    
def dfs(idx,oper_list,oper_num,result,find='max'):
    global max,min
    # print(oper_list)
    global numbers
    # print("result:",result)
    if len(oper_list) == N-1:  # 연산자가 N-1개이면 탈출
        if result>max:
            max=result
        if result<min:
            min=result
        return
    
    if find=='max':  # 현재 값이 최대값 보다 작은데 덧셈 곱셈 연산자가 없을 경우 돌아가기
        if (result<max and oper_num[0]==0 and oper_num[2]==0) or idx>len(numbers)-1:
            return
    if find=='min': # 현재 갑싱 최솟값보다 큰데 뺄셈이나 나눗셈 연산자가 없을 경우 돌아가지
        if (result>min and oper_num[1]==0 and oper_num[3]==0) or idx>len(numbers)-1:
            return
    for i in range(len(oper_num)):
        if oper_num[i]>0:
            oper_list.append(i)   # 연사지 리스트에 추가
            oper_num[i]-=1        # 연산자 개수 줄이기
            if idx==0:   # 인엑스가 0일 경우 앞에 두 개 숫자로 연산
                if i==0:  # 덧셈
                    tmp_res=numbers[0]+numbers[1]
                elif i==1: # 뺄셈 
                    tmp_res=numbers[0]-numbers[1]
                elif i==2: # 곱셈
                    tmp_res=numbers[0]*numbers[1]
                elif i==3: # 나눗셈
                    tmp_res=div(numbers[0],numbers[1])
                dfs(idx+1,oper_list,oper_num,tmp_res,find)
                
            else:   # 인덱스가 0 보다 클 경우 인덱스+1 위치의 값으로 연산
                if i==0:
                    tmp_res=result+numbers[idx+1]
                elif i==1:
                    tmp_res=result-numbers[idx+1]
                elif i==2:
                    tmp_res=result*numbers[idx+1]
                elif i==3:
                    tmp_res=div(result,numbers[idx+1])
                dfs(idx+1,oper_list,oper_num,tmp_res,find)
                
            
            oper_list.pop()  #백트래킹
            oper_num[i]+=1   #백트래킹
            
dfs(0,oper_list,oper_num,0,'max')         
print(max)

dfs(0,oper_list,oper_num,0,'min')

print(min)
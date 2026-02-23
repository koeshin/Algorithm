import sys


total_sum=0

N,M=map(int,sys.stdin.readline().split())

input_list=[]
for i in range(N):
    tmp=sys.stdin.readline().strip()
    tmp_list=[]
    for j in range(M):
        tmp_list.append(int(tmp[j]))
    input_list.append(tmp_list)
    total_sum+=sum(tmp_list)

def get_sum(x_start,x_end,y_start,y_end):
    sum=0
    for i in range(x_start,x_end+1):
        for j in range(y_start,y_end+1):
            sum+=input_list[i][j]
    return sum  



candidate_list=[]

###  가로 분할  ### 
for i in range(N-2):
    for j in range(i+1,N-1):
        s1=get_sum(0,i,0,M-1)
        s2=get_sum(i+1,j,0,M-1)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3)

### 세로 분할  ### 
for i in range(M-2):
    for j in range(i+1,M-1):
        s1=get_sum(0,N-1,0,i)
        s2=get_sum(0,N-1,i+1,j)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3)

### ㅗ 분할 ###  
for i in range(N-1):
    for j in range(M-1):
        s1=get_sum(0,i,0,j)
        s2=get_sum(0,i,j+1,M-1)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3)
### ㅜ 분할 ###
for i in range(N-1):
    for j in range(M-1):
        s1=get_sum(0,i,0,M-1)
        s2=get_sum(i+1,N-1,0,j)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3)
### ㅏ 분할 ###
for i in range(N-1):
    for j in range(M-1):
        s1=get_sum(0,N-1,0,j)
        s2=get_sum(0,i,j+1,M-1)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3) 
### ㅓ 분할 ###
for i in range(N-1):
    for j in range(M-1):
        s1=get_sum(0,i,0,j)
        s2=get_sum(i+1,N-1,0,j)
        s3=total_sum-s1-s2
        candidate_list.append(s1*s2*s3) 

print(max(candidate_list))
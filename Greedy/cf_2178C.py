import sys
import math

t=int(sys.stdin.readline())

def sol_slow(n,n_list): ## O(n^2)으로 time limit 발생
    res=-math.inf
    for i in range(n):
        if i==0:
            tmp_s= -sum(n_list[1:])
        else:
            tmp_s=n_list[0]
            for j in range(1,i):
                
                tmp_s+=abs(n_list[j])
                
            tmp_s+= -sum(n_list[i+1:])


        res=max(res,tmp_s)
        # print('res:',res)

    print(res)

    
    return


def sol_fast(n,n_list): ## O(n^2)으로 time limit 발생
    res=-math.inf
    S=sum(n_list)
    pre_fix_s=0
    
    for i in range(n):
        if i==0:
            S-=n_list[i]
            tmp_s= -S
        else:
            S-=n_list[i]
            
            tmp_s=n_list[0]+pre_fix_s-S
            pre_fix_s+=abs(n_list[i])

        res=max(res,tmp_s)
        # print('res:',res)

    print(res)

    
    return
        

for _ in range(t):
    n=int(sys.stdin.readline())
    n_list=list(map(int,sys.stdin.readline().split()))
    sol_fast(n,n_list)
    
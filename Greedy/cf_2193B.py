import sys


test_num=int(sys.stdin.readline())


def sol(n,n_list):
    
    flag=-1
    f_num=n
    for i in range(n):
        
        tmp=n_list[i]

        if tmp==f_num:
            if flag==-1:
                print(tmp,end=' ')
                f_num-=1
            else:
                for j in range(i,flag-1,-1):
                    print(n_list[j],end=' ')
                flag=-2
        else:
            if flag==-1:
                flag=i
            elif flag==-2:
                print(tmp,end=' ')
                    
                    
for _ in range(test_num):
    n=int(sys.stdin.readline())
    n_list=list(map(int,sys.stdin.readline().split()))
    sol(n,n_list)
    print()
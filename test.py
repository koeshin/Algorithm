import sys



t=int(sys.stdin.readline())


def bin_search(li,val):
    
    low=0
    high=len(li)
    
    
    while low<high:
        mid= (low+high)//2
        
        if li[mid]<=val:
            low=mid+1
        else:
            high=mid
    
    return low

def sol(n,li):
    
    

    s=set(li)


    for k in s:
        tmp=0
        for a in li:
            
            if a!=k-1 and a!=k+1:
                tmp+=1   
    return res


    
    
    
    
    
for _  in range(t):
    n=int(sys.stdin.readline())
    # s=sys.stdin.readline().strip()
    # p,q=list(map(int,sys.stdin.readline().split()))
    # a=list(map(int,sys.stdin.readline().split()))
    # sw=list(map(int,sys.stdin.readline().split()))
    li=list(map(int,sys.stdin.readline().split()))
    # qq=[]
    # for i in range(n):
    #     tmp=list(map(int,sys.stdin.readline().split()))
    #     qq.append(tmp[1:])
    # print('res')
    print(sol(n,li))
    


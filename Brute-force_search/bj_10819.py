import sys


N= int(sys.stdin.readline())

nums=list(map(int,sys.stdin.readline().strip().split()))


def solv_1():
    result=0
    res=[]
    for i in range (len(nums)):
        if len(res)==0:
            tmp_min=min(nums)
            res.append(tmp_min)
            nums.remove(tmp_min)
            continue
        min_a=0
        max_a=0
        flag=0
        tmp_min=min(nums)
        tmp_max=max(nums)
        abs_min=0
        abs_max=0
        min_front=abs(tmp_min-res[0])
        min_back=abs(res[len(res)-1]-tmp_min)
        
        if min_back>min_front:
            min_a=1 
            abs_min=min_back
        else:
            abs_min=min_front
            
        max_front=abs(tmp_max-res[0])
        max_back=abs(res[len(res)-1]-tmp_max)
        
        
        if max_back>max_front:
            max_a=1
            abs_max=max_back
        else:
            abs_max=max_front
        
        if abs_max>abs_min:
            flag=1
            abs_min=abs_max
            
        if flag==0:
            if min_a==0:
                res.insert(0,tmp_min)
            else:
                res.append(tmp_min)
            nums.remove(tmp_min)
        elif flag==1:
            if max_a==0:
                res.insert(0,tmp_max)
            else:
                res.append(tmp_max)
            nums.remove(tmp_max)

        result+=abs_min
        # print(res)
    print(result)
    return

# solv_1()

def solv_2():
    sorted_num=sorted(nums)
    used=[False]*N
    best=0
    
    
    def dfs(depth,last,score):
        nonlocal best
        if depth==N:
            if score>best:
                best=score
            return
        
        prev=None
        for i in range(len(nums)):
            if used[i]:
                continue
            
            if prev==sorted_num[i]: ## 같은 깊이에서 이전과 같은 값은 빼면 최소이므로 건너뛰기
                continue
            
            prev=sorted_num[i]
            used[i]=True
            
            if depth==0:
                dfs(depth+1,sorted_num[i],0)
            else:
                dfs(depth+1,sorted_num[i],score+abs(last-sorted_num[i]))
            used[i]=False ## 백트레킹
    dfs(0,0,0)
    print(best)

    return

solv_2()



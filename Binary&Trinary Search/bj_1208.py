import sys


N,S=map(int,sys.stdin.readline().split())

input_=list(map(int,sys.stdin.readline().split()))

input_.sort()

mid=len(input_)//2
l1=input_[:mid]
l2=input_[mid:]

def left_sum(li):
    
    res = {0: 0}

    for num in li:
        # 현재까지의 결과를 복사하여 루프 도중 변경 방지
        current_items = list(res.items())
        for partial_sum, count in current_items:
            new_sum = partial_sum + num
            # dict.get()이나 'in' 키워드는 O(1)의 속도를 가짐
            res[new_sum] = res.get(new_sum, 0) + 1
    
    if res[0]==0:
        del res[0]
    return res

def right_sum(li,left_sum_list):
    
    res = [0]
    count=0
    for num in li:
        # 현재까지의 결과를 복사하여 루프 도중 변경 방지
        size=len(res)
        for i in range(size):
            new_sum = res[i] + num
            res.append(new_sum)
            # print('new:',new_sum)
            # dict.get()이나 'in' 키워드는 O(1)의 속도를 가짐
            if S-new_sum in left_sum_list:
                count+=left_sum_list[S-new_sum]
            if S==new_sum:
                count+=1
    
  
    return count

left_sum_list=left_sum(l1)
# print(left_sum_list)
result=right_sum(l2,left_sum_list)
if S in left_sum_list:
    result+=left_sum_list[S]
print(result)
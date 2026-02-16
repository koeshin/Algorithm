import sys


N,S=map(int,sys.stdin.readline().split())

input_=list(map(int,sys.stdin.readline().split()))

input_.sort()

mid=len(input_)//2
l1=input_[:mid]
l2=input_[mid:]

def get_sum(li):
    
    res = {0: 1}

    for num in li:
        # 현재까지의 결과를 복사하여 루프 도중 변경 방지
        current_items = list(res.items())
        for partial_sum, count in current_items:
            new_sum = partial_sum + num
            # dict.get()이나 'in' 키워드는 O(1)의 속도를 가짐
            res[new_sum] = res.get(new_sum, 0) + count
    

    return res



left_sum=get_sum(l1)

right_sum=get_sum(l2)

count=0


for k,v in left_sum.items():
    find=S-k
    
    if find in right_sum:
        count+=right_sum[find]*v

if S==0:
    count-=1  ## 둘 다 공집합인 경우 제외

print(count)
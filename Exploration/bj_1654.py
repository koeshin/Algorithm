import sys


K,N=map(int,sys.stdin.readline().split())

high=0
low=1
mid=0

lan_list=[]
for i in range(K):
    tmp=int(sys.stdin.readline().strip())
    lan_list.append(tmp)

lan_list.sort(reverse=True)
high=lan_list[0]
mid=(high+low)//2


#  범위를 정해서 해당 범위 내에서 조검을 만족하는지 확인
while(low<=high):
    # 모든 랜선 mid 길이로 자르기
    mid=(high+low)//2
    sum=0
    for lan in (lan_list):
        sum+=lan//mid
    
    if sum>=N:
        low=mid+1  # 랜선개수를 만들 수 있으면 로우를 미드+1
    else:
        high=mid-1 # 랜선 개수를 만들 수 없으면 하이를 미드-1
print(high)
        
    
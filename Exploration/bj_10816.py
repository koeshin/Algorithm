'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''


import sys
N=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().strip().split()))  # 카드 받기

len_find=int(sys.stdin.readline())  # 찾을 숫자 개수 
find_nums=list(map(int,sys.stdin.readline().strip().split())) # 찾을 숫자들
dict = {num: 0 for num in find_nums} #  각 숫자의 카드가 몇 개 있는지 확인을 위한 딕셔너리

            
for i in range(0,len(cards),2):
    if len(cards)!=1 and i == len(cards)-1:  # 카드 개수가 1개 보다 많고, i가 마지막 카드 인덱스면 탈출(두 개씩 봐서 탈출문 만듬)
        break
    n1=cards[i]    # 첫번째 카드 확인
    
    if n1 in dict.keys():
        dict[n1]+=1   # 각 숫자에 맞게 딕셔너리 값 +1
    if i+1<=len(cards)-1:  # 두 번째 카드 확인
        n2=(cards[i+1])
        if n2 in dict.keys():
            dict[n2]+=1  # 마찬가지로 각 숫자에 딕셔너리  값 +1 
            
# for num in find_nums:       
#     print(dict[num], end=' ')   # 찾는 카드 숫자를 돌면서 딕서너리에서 찾아서 출력




############## Counter 이용하기 ################
## 이게 젤 빠르다
from collections import Counter

count=Counter(cards)

for num in find_nums:
    print(count[num],end=" ")
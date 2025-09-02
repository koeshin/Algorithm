'''
문제
음이 아닌 정수가 N개 들어있는 리스트가 주어졌을 때, 리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 리스트에 포함된 수가 주어진다. 수는 공백으로 구분되어져 있고, 1,000,000,000보다 작거나 같은 음이 아닌 정수 이다. 0을 제외한 나머지 수는 0으로 시작하지 않으며, 0이 주어지는 경우 0 하나가 주어진다.

출력
리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 출력한다. 수는 0으로 시작하면 안되며, 0이 정답인 경우 0 하나를 출력해야 한다.


'''

import sys
import math
N=int(sys.stdin.readline().strip())

lenOfint=10
def duplicate(input,lenOfint):
    k=math.floor(lenOfint/len(input))
    r=lenOfint%len(input)
    res=input*k+input[:r]
    
    return res


dict_not_change={}
dict_change={}
arr=sys.stdin.readline().strip().split()

for i in range(N):
    dict_not_change[i]=(arr[i])
    tmp=(duplicate(arr[i],lenOfint))
    dict_change[i]=tmp

dict_change=sorted(dict_change.items(),key=lambda x:(x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5],x[1][6],x[1][7],x[1][8],x[1][9]),reverse=True)

result=''
for i in range(len(dict_change)):
    dict_change[i]=list(dict_change[i])
    curr=dict_change[i][0]
    result+=dict_not_change[curr]

if result[0]==0:
    print(0)
else:
    print(int(result))
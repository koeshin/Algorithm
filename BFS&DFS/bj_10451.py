import sys

test_case=int(sys.stdin.readline().strip())

res_list=[]
for i in range(test_case):
    test_length=int(sys.stdin.readline().strip())
    numbers=list(map(int,sys.stdin.readline().split()))
    
    tmp={}
    
    for j in range(1,len(numbers)+1):
        tmp[j]=numbers[j-1]
    
    res=0
    key_list=[_ for _ in range(1,test_length+1)]
    
    cic=[]
    

    idx=key_list[0]
    while (len(key_list)>0):
        if idx in cic:
            res+=1
            idx=key_list[0]
            cic.clear()

        cic.append(idx)
        key_list.remove(idx)
        idx=tmp[idx]
    res_list.append(res+1)

for res in res_list:
    print(res)
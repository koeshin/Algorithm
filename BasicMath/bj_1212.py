import sys

bits=input().strip()
res=[]

idx=0
for bit in bits:
    
    
    tmp=int(bit)
    for i in range(3):
        cur=2**(2-i)
        if tmp//cur>0:
            tmp-=cur
            res.append(str(1))
        else:
            if len(res)>0:  # 주의: res 리스트가 비어있으면, 맨 앞자리가 0 이 될 수 있음. 그걸 방지해야함.
                res.append(str(0))

if bits == '0': ## 주의: 이거 처리하지않으면 0일 경우 빈칸이 출력됨.
    res.append(str(0))

print(''.join(res))
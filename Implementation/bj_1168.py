import sys
import math
N,M=map(int,sys.stdin.readline().split())


seg_t=[0]*(4*N+1)

def init(node,s,e):
    if s==e:
        seg_t[node]=1
        return seg_t[node]
    mid=(s+e)//2
    seg_t[node]=init(2*node,s,mid)+init(2*node+1,mid+1,e)
    return seg_t[node]


    
def query(node,s,e,idx):
    seg_t[node]-=1
    if s==e:
        return s
    
    mid=(s+e)//2
    if idx>seg_t[2* node]:
        return query(2*node+1,mid+1,e,idx-seg_t[2*node])
    else:
        return query(2*node,s,mid,idx)


init(1,1,N)

idx=1
print('<',end='')
for i in range(N):
    size=N-i
    # 다음 순서(index) 계산
    idx += M - 1
    if idx % size == 0:
        idx = size
    elif idx > size:
        idx %= size
    res=query(1,1,N,idx)
    
    if i<N-1:
        print(f'{res},',end=" ")
    else:
        print(f'{res}>')
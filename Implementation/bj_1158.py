import sys

N,M=map(int,sys.stdin.readline().split())

qq=[]
for i in range(1,N+1):
    qq.append(i)
    

idx=0
print('<',end='')
while qq:
    idx=(idx+M-1)%len(qq)
    tmp=qq.pop(idx)
    if  len(qq)>0:
        print(f'{tmp},',end=' ')
    else:
        print(f'{tmp}',end='')
print('>')
    
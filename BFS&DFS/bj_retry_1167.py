import sys
sys.setrecursionlimit(10000000)
N=int(sys.stdin.readline())

tree=[[] for _ in range(N+1)]

for i in range(N):
    tmp=list(map(int,sys.stdin.readline().split()))
    point=tmp[0]
    for i in range(1,len(tmp)-1,2):
        tu=(tmp[i],tmp[i+1])
        tree[point].append(tu)

global res
res=0
def dfs(point,visited):
    global res
    visited[point]=True
    lengths=[]
    for tuple in tree[point]:
        k=tuple[0]
        v=tuple[1]
        if visited[k] is False:
            t=dfs(k,visited)
            lengths.append(v+t)
    lengths.sort(reverse=True)
    if len(lengths)>=2:
        res=max(res,lengths[0]+lengths[1])
        return lengths[0]
    elif len(lengths)==1:
        res=max(res,lengths[0])
        return lengths[0]
    else:
        return 0
        



visited=[False]*(N+1)
dfs(i,visited)
print(res)
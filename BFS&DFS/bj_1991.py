import sys


N=int(sys.stdin.readline())


tree={}
for i in range(N):
    tmp=sys.stdin.readline().strip().split()

    tree[tmp[0]]=[tmp[1],tmp[2]]
    

def DFS_pre(start):
    print(start,end='')
    if tree[start][0]!='.':
        DFS_pre(tree[start][0])
    
    if tree[start][1]!='.':
        DFS_pre(tree[start][1])

    return

def DFS_mid(start):
    

    
    if tree[start][0]!='.':
        DFS_mid(tree[start][0])
    
    print(start,end='')
    if tree[start][1]!='.':
        DFS_mid(tree[start][1])
    
    return

def DFS_back(start):
    

    
    if tree[start][0]!='.':

        DFS_back(tree[start][0])

    if tree[start][1]!='.':

        DFS_back(tree[start][1])
        
    print(start,end='')
    
    return

DFS_pre('A')
print()
DFS_mid('A')
print()
DFS_back('A')
print()
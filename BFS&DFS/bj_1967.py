import sys

sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline())

trees={}
weights={}
for i in range(N-1):
    a,b,c = list(map(int,sys.stdin.readline().strip().split()))

    if a not in trees.keys():
        trees[a]=[b]
        weights[a]=[c]
    else:
        trees[a].append(b)
        weights[a].append(c)
        

# print(trees)
# print(weights)
global result
result=0

def DFS(node):
    global result
    
    child_total_weight=[]
    max_child_weight=0
    if node in trees.keys():
        
        for ch,we in zip(trees[node],weights[node]):
            # print('ch:',ch)
            # print('we',we)
            child_weight=DFS(ch)
            child_weight+=we
            max_child_weight=max(max_child_weight,child_weight)
            child_total_weight.append(child_weight)
        
        child_total_weight.sort(reverse=True)
        
        # print(child_total_weight)
        if len(child_total_weight)>1:
            result=max(result,child_total_weight[0]+child_total_weight[1])
        else:
            result=max(result,child_total_weight[0])
        return max_child_weight
    else:
        return 0
    
DFS(1)

print(result)
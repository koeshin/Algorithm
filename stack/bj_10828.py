import sys

N=int(sys.stdin.readline())

stack=[]

for i in range(N):
    commands=sys.stdin.readline().split()
    comm=commands[0]
    if comm.startswith("pu"):
        num=commands[1]
        stack.append(int(num))
        
    elif comm.startswith("po"):
        if stack:
            tmp=stack.pop()
            print(tmp)
        else:
            print(-1)
    elif comm.startswith("si"):
        print(len(stack))
        
    elif comm.startswith("em"):
        if not stack:
            print(1)
        else:
            print(0)
    elif comm.startswith("to"):
        if stack:
            print(stack[-1])
        else: 
            print(-1)
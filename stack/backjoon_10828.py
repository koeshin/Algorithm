import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for i in range(n)]


list=[]
for i in range(n):

    order=data[i][0]
    
    if order == "push":
        list.append(data[i][1])
    elif order == "pop":
        if len(list) == 0:
            print(-1)
        else:
            print(list[len(list)-1])
            list.pop()
            
    elif order == "size":
        print(len(list))
    elif order == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(list) == 0:
            print(-1)
        else:
            print(list[len(list)-1])


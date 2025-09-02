import sys

max_=100

res=[]
for i in range(max_):
    input_=sys.stdin.readline().strip()
    if input_=='':
        break
    else:
        res.append(input_)

for r in res:
    print(r)
    
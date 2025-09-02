import sys

n=int(sys.stdin.readline().strip())

numbers=sys.stdin.readline().strip()

res=0
for i in range(n):
    res+=int(numbers[i])
    
print(res)
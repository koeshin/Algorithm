import sys

N=int(sys.stdin.readline())


for  i in range(1,2*N):
    if i<= N:
        stars=i
        blank=2*(N-i)
    else:
        stars=2*N-i
        blank=2*(i-N)
    
    print("*"*stars+" "*blank+"*"*stars) 
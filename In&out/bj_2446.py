import sys

N=int(sys.stdin.readline())


for i in range(2*N):
    
    if i<N:
        tmp=N-i
        print(" "*i+'*'*(2*tmp-1))
    elif i>N:
        tmp=i-N
        print(" "*(N-1-i%N)+'*'*(2*(tmp+1)-1))
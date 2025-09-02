import sys

N= int(sys.stdin.readline())

for i in range(N):

    if i==N-1:
        print('*'*(2*N-1))
        break
    else:
        if i ==0: 
            print(" "*(N-1)+"*")
        else:
            first_blank=N-i-1
            second_blank=(2*N-1) - (N-i-1)*2 -2
            print(" "*first_blank+"*"+" "*second_blank+"*")


import sys



num=sys.stdin.readline().strip()

zero_flag=0
sum_=0
num_list=[]
for str in num:
    if int(str) ==0:
        zero_flag=1
    
    sum_+=int(str)
    num_list.append(int(str))

if sum_%3==0:
    if zero_flag==1:
        num_list.sort(reverse=True)
        print(num_list)
        for n in num_list:
            print(n,end='')
    else:
        print(-1)
else:
    print(-1)
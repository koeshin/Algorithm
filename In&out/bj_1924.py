import sys


mon,day=map(int,sys.stdin.readline().split())

day_of_week=['MON',"TUE","WED","THU","FRI","SAT","SUN"]

total_days=0
for i in range(1,mon):
    if i in [1,3,5,7,8,10,12]:
        days=31
        
    elif i in [4,6,9,11]:
        days=30
        
    elif i == 2:
        days=28
        
    total_days+=days


k=(total_days+day-1)%7

print(day_of_week[k])



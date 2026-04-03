import sys


while(True):
    tmp=sys.stdin.readline()
    if tmp == "":      # ✅ EOF 처리
        break
    if tmp.isspace():
        break
    lower_cnt=0
    upper_cnt=0
    num_cnt=0
    blank_cnt=0
    
    for char in tmp:
        if char.islower():
            lower_cnt+=1
        elif char.isupper():
            upper_cnt+=1
        elif char==' ':
            blank_cnt+=1
        elif char.isdigit():
            num_cnt+=1
    print(f"{lower_cnt} {upper_cnt} {num_cnt} {blank_cnt}")
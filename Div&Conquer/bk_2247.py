import sys


global N
N=int(sys.stdin.readline().strip())

def make_star(n):
    
    if n==1:
        return ['*']
    star=make_star(n//3)
    
    stars=[]
    
    for a in star:
        stars.append(a*3)  # 첫 번째 층 이전 결과를 3개씩 복사해서 stars에 추가
    for b in star:
        stars.append(b+" "*(n//3)+b) # 두 번째 층 이전 결과에 빈 공간을 추가해서 stars에 추가
    for c in star:
        stars.append(c*3)  # 첫번째 층과 동일

    return stars



stars=make_star(N)
for star in stars:
    print(star)
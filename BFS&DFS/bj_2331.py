import sys

A, P = sys.stdin.readline().split()
P = int(P)

cur = A
visited = {int(A): 0}  # 시작 값 A를 0번 인덱스로 저장
idx = 1                # 다음에 나올 수는 인덱스 1부터 시작

while True:
    tmp = 0
    for n in cur:
        tmp += int(n) ** P   # 다음 수 계산

    if tmp in visited:
        # tmp가 처음으로 다시 나온 수
        end = visited[tmp]   # 그 수의 처음 등장 인덱스 = 정답
        break

    visited[tmp] = idx
    idx += 1
    cur = str(tmp)

print(end)

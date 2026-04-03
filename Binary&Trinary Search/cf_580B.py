import sys

def solve():
    # 1. 입력 최적화: 모든 입력을 한 번에 메모리로 읽어와 파싱 (I/O 병목 제거)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    d = int(input_data[1])
    
    # 2. 친구 정보 리스트 생성: (돈, 우정 점수) 튜플 형태로 저장
    friends = []
    idx = 2
    for _ in range(n):
        friends.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    # 3. '돈(money)'을 기준으로 오름차순 정렬 (O(N log N))
    friends.sort(key=lambda x: x[0])
    
    # 4. 투 포인터 변수 초기화
    left = 0
    current_friendship = 0
    max_friendship = 0
    
    # right 포인터를 0부터 n-1까지 이동 (O(N))
    for right in range(n):
        # 윈도우에 새로운 친구를 추가하고 우정 점수를 누적
        current_friendship += friends[right][1]
        
        # 5. 조건 검사: 그룹 내 최대 빈부격차가 d 이상인지 확인
        # 차이가 d 이상이라면, 조건을 다시 만족(차이가 d 미만)할 때까지 left 포인터를 오른쪽으로 이동
        while friends[right][0] - friends[left][0] >= d:
            current_friendship -= friends[left][1] # 윈도우에서 제외되는 친구의 우정 점수 차감
            left += 1
            
        # 6. 매 순간 조건을 만족하는 윈도우의 우정 점수 최댓값을 갱신
        if current_friendship > max_friendship:
            max_friendship = current_friendship
            
    # 최종 최댓값 출력
    print(max_friendship)

if __name__ == '__main__':
    solve()
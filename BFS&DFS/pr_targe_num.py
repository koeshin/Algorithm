answer=0
def solution(numbers, target):
    global answer

    def dfs(input, numbers, target):
        global answer
        if len(input) == len(numbers):
            sum = 0
            for i in range(len(input)):
                sum += input[i] * numbers[i]
            if sum == target:
                answer += 1

            return 
        tmp = [1, -1]

        for k in tmp:
            tmp_input = input.copy()
            tmp_input.append(k)
            dfs(tmp_input, numbers, target)  # 재귀 호출 결과를 업데이트
        return 

    dfs([1], numbers, target)
    dfs([-1], numbers, target)

    return answer


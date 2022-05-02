def find_min(*args):
    min_r = args[0]
    min_index = 0
    for idx, arg in enumerate(args):
        if arg < min_r:
            min_r = arg
            min_index = idx

    return min_index, min_r


def find_max(*args):
    max_r = args[0]
    max_index = 0
    for idx, arg in enumerate(args):
        if arg > max_r:
            max_r = arg
            max_index = idx

    return max_index, max_r


def sum_num(*args):
    result = 0
    for arg in args:
        result += arg
    return result


import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0210_input.txt", 'r')

for tc in range(1, 11):
    # 1. input
    dump = int(input())

    arr = list(map(int, input().split()))

    # 2. 평탄화가 완료될 경우의 높이
    completed_height = sum_num(*arr) // 100
    completed = False
    completed_diff = None

    # 2. min, max 찾아서 올기기
    while dump > 0:
        max_index, max_value = find_max(*arr)
        min_index, min_value = find_min(*arr)
        # 끝나지 않은 경우
        if min_value < completed_height:
            arr[max_index] -= 1
            arr[min_index] += 1

        # 끝난 경우
        else:
            completed = True
            # 평탄화 결과가 평평한 경우
            if max_value == min_value:
                completed_diff = 0
                break

            # 평탄화 결과가 평평하지 않은 경우
            else:
                completed_diff = 1
                break
        dump -= 1

    if completed == False:
        completed_diff = max_value - min_value

    print(f"#{tc} {completed_diff}")

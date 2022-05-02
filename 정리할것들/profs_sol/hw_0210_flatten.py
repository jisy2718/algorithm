import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0210_input.txt", 'r')


T = 10
for tc in range(1,T+1):
    # 너비
    N = int(input())
    # 건물들의 높이
    arr = list(map(int,input().split()))

    for _ in range(N):
        max_index = 0
        min_index = 0
        for i in range(100): # 상자 높이 중 최고, 최저 찾기 반복문
            if boxes[i] > boxes[max_idx]:
                max_idx = i
            if boxes[i] < boxes[min_idx]:
                min_idx = i

        # 반복문이 끝나면 최고 높이와 최저 높이의 위치를 알 수 있음
        # 덤프작업
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    # 반복문이 끝나면 덤프작업이 완료됨
    max_idx = 0
    min_idx = 0
    for i in range(100): # 상자 높이 중 최고, 최저 찾기 반복문
        if boxes[i] > boxes[max_idx]:
            max_idx = i
        if boxes[i] < boxes[min_idx]:
            min_idx = i

    print(f"#{tc} {boxes[max_idx]-boxes[min_idx]}")
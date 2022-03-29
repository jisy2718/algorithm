import sys
# 표준 입력 경로 변경
sys.stdin = open("4836_sample_input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    red = set()
    blue = set()

    for row in range(N):
        # red case
        if arr[row][-1] == 1:
            left_top_x = arr[row][0]
            left_top_y = arr[row][1]
            right_bottom_x = arr[row][2]
            right_bottom_y = arr[row][3]

    # red set에 red coordinate 추가
            for coor_x in range(left_top_x, right_bottom_x + 1):
                for coor_y in range(left_top_y, right_bottom_y + 1):
                    red.add((coor_x, coor_y))
                    #print(red)
# blue case
        if arr[row][-1] == 2:
            left_top_x = arr[row][0]
            left_top_y = arr[row][1]
            right_bottom_x = arr[row][2]
            right_bottom_y = arr[row][3]

# blue set에 blue coordinate 추가
            for coor_x in range(left_top_x, right_bottom_x + 1):
                for coor_y in range(left_top_y, right_bottom_y + 1):
                    blue.add((coor_x, coor_y))

    # 교집합의 원소개수 세기
    intersection = len(red) - len(red - blue)
    print(f"#{tc} {intersection}")
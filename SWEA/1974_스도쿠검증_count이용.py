import sys
sys.stdin = open('1974_input.txt')


def check_sdoku(arr):
    # 검사한 9x9 행렬이 스도쿠라면 True, 아니라면 False
    # 행 우선 순회
    result = True
    for r in range(9): # 행 index
        count = [0]*10
        for c in range(9): # 열 index
            if count[arr[r][c]] == 0:
                count[arr[r][c]] = 1
            else:
                return False

    # 열 우선 순회
    for c in range(9): # 열 index
        count = [0]*10
        for r in range(9): # 행 index
            if count[arr[r][c]] == 0:
                count[arr[r][c]] = 1
            else:
                return False

    # 3x3 순회
    for r in range(0,9,3):
        for c in range(0,9,3):
            count = [0]*10
            for rr in range(3):
                for cc in range(3):
                    if count[arr[r+rr][c+cc]] == 0:
                        count[arr[r + rr][c + cc]] = 1
                    else:
                        return False

    return True




T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    result = check_sdoku(arr)

    print(f"{tc} {int(result)}") # true 면 1, false 면 0

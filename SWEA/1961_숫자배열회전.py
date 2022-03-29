import sys
sys.stdin = open('1961_input.txt')

# 2차원 정사각배열 90' 회전 함수
def rotation(arr):
    arr_90 = []
    N = len(arr)

    for c in range(N):
        new_row = []
        for r in range(N-1,-1,-1):
            new_row.append(arr[r][c])
        # print(f"{c+1}-th row is {new_row}")
        arr_90.append(new_row)
    return arr_90



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # print(f"N is {N}")
    arr = [list(input().split()) for _ in range(N)]
    # print(f"arr is {arr}")

    list_of_arrs = []
    # for i in range(1,4): # 90, 180, 270 도 회전 결과를 list_of_arrs 에 추가
    #     rotated_arr = []
    #     for _ in range(i):
    #         rotated_arr = rotation[arr]

    list_of_arrs.append(rotation(arr))
    list_of_arrs.append(rotation(rotation(arr)))
    list_of_arrs.append(rotation(rotation(rotation(arr))))

    # 출력
    print(f"#{tc}")
    for r in range(N):
        for arr in list_of_arrs:
            print(''.join(arr[r]), end=' ')
        print()
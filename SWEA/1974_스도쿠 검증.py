import sys
sys.stdin = open('1974_input.txt')


T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    flag = True

    # 1) 행과 열 순회
    # 행과 열 한 번에 순회
    for i in range(9):
        # set 으로 중복여부 확인
        set_row = set()
        set_col = set()

        # row, col 각각 이동
        for j in range(9):
            if (arr[i][j] in set_row) or (arr[j][i] in set_col):
                flag =False
                break
            else:
                set_row.add(arr[i][j])
                set_col.add(arr[j][i])

    # if flag == False:
    #     break

    else: # flag 가 True인 경우만, 3x3 정사각형 순회
        # 시작지점 9 군데를 for문으로 생성
        for i in [0,3,6]:
            for j in [0,3,6]:
                set_sq = set()  # 3x3 블록의 set 초기화
                for ii in range(3):
                    for jj in range(3):
                        if arr[i+ii][j+jj] in set_sq:
                            flag = False
                            break
                        else:
                            set_sq.add(arr[i+ii][j+jj])
                    if flag == False:
                        break
                if flag == False:
                    break
            if flag == False:
                break

    print(f"#{tc} {int(flag)}")


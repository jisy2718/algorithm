from collections import deque
import sys
sys.stdin = open("5188_input.txt")


def dfs(r, c, cur_sum):
    global min_sum
    if min_sum < cur_sum:
        return

    if r == er and c == ec and min_sum > cur_sum:
        min_sum = cur_sum

    else:
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc, cur_sum + arr[nr][nc])


# 이동 규칙/ 우, 하
dr = [0, 1]
dc = [1, 0]




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]

    # 시작, 종료점
    sr, sc = 0, 0
    er, ec = N - 1, N - 1
    cur_sum = arr[sr][sc]


    # 결과
    min_sum = 13*2*10


    dfs(sr, sc, cur_sum)
    print(f"#{tc} {min_sum}")




    # # BFS--------------------------------------------
    # queue = deque([[sc, sr, cur_sum]])
    # # print(queue)
    #
    # while queue:
    #     cr, cc, cs = queue.popleft()
    #
    #     if cr == er and cc == ec:
    #         if min_sum > cs:
    #             min_sum = cs
    #
    #     for i in range(2):
    #         nr = cr + dr[i]
    #         nc = cc + dc[i]
    #         if 0 <= nr < N and 0 <= nc < N:
    #             queue.append([nr, nc, cs + arr[nr][nc]])
    #             # print(queue)
    #
    # print(f"#{tc} {min_sum}")
    # #--------------------------------------------


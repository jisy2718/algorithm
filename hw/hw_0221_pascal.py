# sol1  ) recursion

# r은 행, c는 열 순서
def pascal(r, c):
    #global count
    #count += 1
    if c == 1 or r == c or r == 1:
        return 1

    else:
        return pascal(r - 1, c - 1) + pascal(r - 1, c)


T = int(input())

for tc in range(1, T + 1):
    #count = 0
    N = int(input())
    for r in range(1, N + 1):
        for c in range(1, r + 1):
            print(pascal(r, c), end=' ')
        print()
    #print(f"total count is {count}")

#-------------------------------------------------------------------------
# sol2) memoization
# r은 행, c는 열 순서
def pascal(r, c):
    # base line으로 1행이되거나 각 행의 양 끝열이 되면 return 1
    global memo
    #global count
    #count += 1
    if c == 1 or r == c or r == 1:
        memo[r][c] = 1
        return 1

    # r,c 위치의 값은 r-1,c-1 위치의 값 + r-1,c 위치의 값
    else:
        if memo[r][c] == 0:
            memo[r][c] = pascal(r - 1, c - 1) + pascal(r - 1, c)
    return memo[r][c]


T = int(input())

for tc in range(1, T + 1):
    # 행의 개수
    N = int(input())

    memo = [[0] * (N + 1)] + [[0] + [0] * N for _ in range(N)]
    count = 0
    print(f"#{tc}")
    for r in range(1, N + 1):  # r 행의 숫자 출력
        for c in range(1, r + 1):
            print(pascal(r, c), end=' ')
        print()

    #print(f"total count is {count}")
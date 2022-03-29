T = int(input())
for tc in range(1, T + 1):
    p = input()  # 찾을 패턴
    total = input()  # 전체 text

    # 고고한방법
    i, j = 0, 0
    n = len(total)  # 전체 text 길이
    m = len(p)  # 찾을 패천의 길이

    # 패턴의 끝까지 갈때까지 or text를 전부 탐색할 때까지
    while j < m and i < n:  # 0 1 2 3 4 5 / 0 1 2

        if total[i] != p[j]:
            j = -1

        i += 1
        j += 1
        # print(f"#2---------i,j : {i},{j}")

    if j == m:
        print(1)

    else:
        print(0)
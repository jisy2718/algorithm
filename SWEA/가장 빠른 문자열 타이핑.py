T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    N, M = len(A), len(B)
    count = 0
    i = 0
    while i < N:
        # 같은 경우
        if A[i:i + M] == B:
            count += 1
            i += M
        else:  # 다른 경우
            count += 1
            i += 1

    print(f"#{tc} {count}")
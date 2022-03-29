import sys
# 표준 입력 경로 변경
sys.stdin = open("5789_input.txt", 'r')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, Q = list(map(int, input().split()))

    l = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L,R+1):
            l[j] = i


    print(f"#{tc}", *l[1:])
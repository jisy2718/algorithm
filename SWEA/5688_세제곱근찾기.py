T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 반씩 숫자 줄여나가면서 찾기
    # 반 줄인 숫자**3 보다 N이 크면 큰 쪽으로 반 줄이고, N 이 작으면 작은 쪽으로 반 줄이기
    left = 0  # 후보군 중 왼쪽 끝
    right = N # 후보군 중 오른쪽 끝
    mid = N // 2
    while True:
    # for _ in range(5):
        if mid**3 < N: # mid가 커져야 함. 그래서 기존 mid를 left로 두고, mid를 증가시킨다
            left = mid
            mid = (mid+right)//2

        elif mid**3 > N:
            right = mid
            mid = (left+mid)//2

        elif mid**3 == N:
            result = mid
            break

        if left == mid: # left**3 < N < (left+1)**3 경우우
            result = -1
            break
        # print(mid)
    if N == 1:
        result = 1
    print(f'#{tc} {result}')
import sys
sys.stdin = open('1979_input.txt')

# 행방향으로 1이 정확히 K 개 연속된 것 개수 세는 함수 : arr에 더미로 0 인 행, 열 추가해준 후 함수에 넣기
def find_space(arr, K):
    N = len(arr)
    result = 0

    for r in range(N-1):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
    return result


T = int(input())

for tc in range(1,T+1):
    N, K = list(map(int,input().split()))
    arr = [list(map(int,input().split())) +[0] for _ in range(N)]
    arr.append([0]*(N+1))
    result = 0
    arr_t = list(map(list,zip(*arr)))
    result += find_space(arr, K) + find_space(arr_t, K)

    print(f"#{tc} {result}")



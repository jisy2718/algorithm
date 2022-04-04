# import sys
# sys.stdin = open("2117_input.txt")
def sub_set(L):

    results = []
    for i in range(1<<len(L)): # 부분집합 개수로 이진수라고 생각
        result = []
        for j in range(len(L)):
            if i & (1<<j):
                result.append(L[j])
        results.append(result)
    return results



def max_benefit(L):
    results = sub_set(L)
    ans = 0
    for l in results:

        benefit = 0
        c = 0
        i = 0
        while i < len(l):
            c += l[i]
            if c > C:
                break
            benefit += l[i]**2
            # print(c, benefit)
            i += 1
        ans = max(ans,benefit)

    return ans



T = int(input())

for tc in range(1,T+1):

    # N : NxN 벌통 배열, M : 한 행에서 채취할 수 있는 벌통 개수(벌통단위로만 채취), C : 한 행에서 최대채취 가능 양
    N, M, C = map(int,input().strip().split())  # 각 벌통의 꿀의 양은 1~9 /  N >= M
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    memo = [[0]*N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            memo[i][j] = max_benefit(arr[i][j:j+M])
    #
    # for row in arr:
    #     print(row)
    # for row in memo:
    #     print(row)

    ans = 0
    for i1 in range(N):
        for j1 in range(N):
            ans1 = memo[i1][j1]

            for i2 in range(i1,N):
                sj = 0
                if i1==i2:
                    sj = j1+M
                for j2 in range(sj, N):
                    ans2 = memo[i2][j2]
                    ans = max(ans,ans1+ans2)

    print(f"#{tc} {ans}") # 제곱수



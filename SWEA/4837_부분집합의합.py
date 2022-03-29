import sys
sys.stdin = open("4837_sample_input.txt")

T = int(input())
A = list(range(1,13))
for tc in range(1,T+1):
    N, K = tuple(map(int,input().split()))
    length = len(A)
    total_count = 0 #전체 결과
    for i in range(1<<length): # 전체 부분집합
        bit_count = 0
        cur_sum = 0
        for j in range(length): # A 의 i번재 비트자리의 포함 유무
            if i & (1<<j):
                bit_count += 1 # i 번째 비트를 포함한다면, bit_count에  반영
                cur_sum += A[j]
        if bit_count == N and cur_sum == K :
            total_count += 1
    print(f"#{tc} {total_count}")
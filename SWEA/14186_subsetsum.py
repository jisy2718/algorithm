N = int(input())

arr = list(map(int,input().split()))
result = 0
for i in range(1<<N): # 전체 2^N개의 부분집합을 이진수표현으로 생각 (i가 이진수라 생각)
    sub_set_sum = 0
    for j in range(N):
        if i & (1<<j):  # j 번째 비트가 1이면 j번째 원소를 부분집합에 포함
            sub_set_sum += arr[j]
    if sub_set_sum == 0:
        result += 1

print(result)

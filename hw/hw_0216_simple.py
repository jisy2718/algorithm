import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0216_input.txt", 'r')



alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


T = int(input())
for _ in range(1,T+1):
    # 1. input
    tc , N = input().split()
    N = int(N)

    arr = input().split()
    result = list()
    for i in range(10):
        for j in range(N):
            if alien[i] == arr[j]:
                result.append(arr[j])

    print(tc)
    print(*result)
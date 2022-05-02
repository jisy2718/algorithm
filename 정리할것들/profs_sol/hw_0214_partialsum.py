import sys
sys.stdin = open("hw_0214_input.txt",'r')

for _ in range(10):
    tc = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]



    # 3. 2차원 배열의 대각선 순회 ( 변수 2개 필요 )

    # 3-1 방법 1) # 직접 대각선 합 코딩
    # 대각선 1: i == j
    # 대각선 2 : i + j = 99


    # 3-2 방법 2) # 행/열 순회할 때 대각선원소를 지나면 더해주기
    max_sum = 1<<40
    dia1_sum = 0
    dia2_sum = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            if i == j :
                dia1_sum += arr[i][j]
            if i + j == 99:
                dia2_sum += arr[i][j]

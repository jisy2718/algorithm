import sys
# 표준 입력 경로 변경
sys.stdin = open("6485_input.txt", 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    count = [0]*5001
    for _ in range(N):
        start, end = map(int,input().split())
        for i in range(start,end+1):
            count[i] += 1

    result = []
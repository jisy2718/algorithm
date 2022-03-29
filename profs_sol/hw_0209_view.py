#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV134DPqAA8CFAYh&probBoxId=AX7cgLH6Z7UDFAS2+&type=PROBLEM&problemBoxTitle=22020_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=++1+

import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0209_input.txt", 'r')


T = 10
for tc in range(1,T+1):
    # 너비
    N = int(input())
    # 건물들의 높이
    arr = list(map(int,input().split()))

    # 건물을 하나씩 확인하면서 조망권이 확복된 세대의 수를 누적합
    cnt = 0
    for i in range(2, N-2): # 양쪽 끝 2개씩 건물이 없음
        # arr[i] : i 번째 건물의 높이
        # i 번재 건물의 조망권 계산
        # 조망권이 확보된 세대 수 : 현재 건물 높이 - 주변 건물 중 가장 높은 건물 높이 > 0 인 경우
        # result = arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

        # 반복문으로 최대값 구하기
        max_value = 0
        for j in range(i-2, i+3):
            if arr[j] > max_value and j!= i:
                max_value = arr[j]
            result =  arr[i] - max_value

        if result > 0:
            cnt += result


    print(f"#{tc} {cnt}")

import sys
# 표준 입력 경로 변경
sys.stdin = open("5432_input.txt", 'r')

T = int(input())

for tc in range(1,T+1):
    lst = input()
    result = 0 # 전체결과
    cnt = 0   # 현재 막대개수

    # 조건에 맞게 cnt, result 조작
    for i in range(len(lst)):

        # 막대기 시작 경우
        if lst[i] == '(':
            cnt += 1

        # 레이저 경우 / 막대 닫힘
        else: # lst[i] == ')'
            # 레이저
            if lst[i-1] == '(':
                cnt -= 1  # 첫 if문에서 센 것 줄이기
                result += cnt # 현재 막대수 만큼 추가
            # 막대 닫힘
            else: # lst[i-1]== ')' 막대의 끝
                cnt -= 1
                result += 1
    print(f"#{tc} {result}")
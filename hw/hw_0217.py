import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0217_input.txt", 'r')

# 각 행 지정
# 행의 첫부분 부터 순회 index ; i
# 행의 뒷부분부터 index i 에 해당하는 문자 있는지 판단 : index j
# 만약 다르다면 계속 진행 until i <= j
# 만약 같다면, 회문인지 파악 진행 , : i index 증가, j index 감소 : i,j 모두 while로 해야함 until
# 회문의 출발 index 와 끝의 index를 알수 있도록 하기

T = 10

for tc in range(1,11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_t = list(zip(*arr)) # 내부는 튜플이지만 계산에 문제 없음
    max_length = 1 # 회문 없는 경우 값
    for cur_arr in [arr, arr_t]:
        for row in cur_arr:  # 행선택
            for i in range(99):  # 행에서 회문 시작 문자 선택
                if 99 - i < max_length:# 만약 현재 가능한 최대길이가 기존의 회문 최대길이보다 같거나 작다면 i for문 break
                    break
                for j in range(99,i, -1): # 행에서 회문 마지막 문자 선택

                    # 만약 현재 가능한 최대길이가 기존의 회문 최대길이보다 같거나 작다면 j for문 break
                    if max_length >= j - i + 1:
                        break
                    # 회문의 시작과 끝
                    start = i
                    end = j

                    while i < j: # j 가 아직 i보다 큰 경우는 회문 판정이 끝나지 않은 것
                    # 회문형태인 경우
                        if row[i] == row[j]:
                            i += 1
                            j -= 1
                    # 회문형태가 아닌경우 j를 감소시킴
                        else:
                            i = start # i 초기화 및 j 는 다음 인덱스로
                            break
                    # 회문을 찾은 경우 max 길이 비교
                    if i >= j:
                        if max_length < end - start +1:
                            max_length = end - start + 1

    print(f"#{tc} {max_length}")
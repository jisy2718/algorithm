import sys
sys.stdin = open('1859_input.txt')


# max를 찾는 함수 만들기
def find_max_index(lst:list):
    if not lst:
        print("no element in input lst")
        return
    else:
        max_index = 0
        for i in range(1, len(lst)):
            if lst[max_index] <= lst[i]: # max 중복시 뒤에것 선택
                max_index = i
        return max_index




T  = int(input())

for tc in range(1,T+1):
    N = int(input()) # 받는 배열의 길이
    arr = list(map(int,input().split()))
    result = 0 #이익금
    # 반복횟수 정해져 있지 않으므로, while 문 이용
    i = 0 # lst에 indexing 할 초기 값으로 lst의 start index
    while i < len(arr):  # i가 끝을 넘어가면 그만
        # i는 현재 시작 index
        max_index = find_max_index(arr[i:]) + i # arr 에서 max_index로 이 이하의 값들은 모두 팔면 됨
        max_value = arr[max_index]
        # 현재 시작과 끝
        for j in range(i, max_index+1):# 다 더해주기 /  max_index = i 인 경우에도 문제 없음
            result += ( max_value - arr[j] )

        # i 값 재설정
        i = max_index + 1

    print(f"#{tc} {result}")


import sys
sys.stdin = open('4408_input.txt')


def find_min_max(a,b):
    if a > b:
        return b, a
    else:
        return a, b


T = int(input())



for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    count = [0] * 201 # 맨 앞 0은 더미

    for one_student in arr:
        # 지나가는 복도 count의 인덱스로 바꿔주기
        # 홀수는 +1 더한후 //2
        # 짝수는 //2
        for i in range(2):
            if one_student[i]%2:#홀수
                one_student[i] = (one_student[i]+1)//2
            else:
                one_student[i] //= 2

        # count에서 시작, 끝 index
        start, end = find_min_max(one_student[0], one_student[1])

        # 지나는 복도 index에서 count 에 +1
        for i in range(start,end+1):
            count[i] += 1

    # count 중 max 찾으면 됨
    max_val = 0
    for num in count:
        if max_val < num:
            max_val = num

    print(f"#{tc} {max_val}")

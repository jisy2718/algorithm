N = int(input())  # input 개수
l = [0] * N  # 길이 N인 list 생성

# N개 의 수를 l에 저장
for i in range(N):
    l[i] = int(input())

# 음아닌 정수로 만들기
for i in range(len(l)):
    l[i] += 1000

# 정렬 알고리즘 적용
## counting sort 적용
result = [0] * N
count = [0] * 2001  # 0 ~ 2000 까지의 수에 적용

## l 의 각 숫자가 몇 번 나오는 지 count
for num in l:
    count[num] += 1
    # print(f"length of count: {len(count)}")

## count 를 누적 시킴
for i in range(1, 2001):
    count[i] += count[i - 1]  # count[2000] = len(l) 이 됨.

## l의 각 num을 result에 알맞은 위치에 하나씩 추가하기
for num in l:
    result_index = count[num] - 1  # result에서 해당 num들 중 가장 마지막 위치

    result[result_index] = num

# 원래의 수 범위로 바꾸기
for i in range(len(result)):
    result[i] -= 1000
for sorted_num in result:
    print(sorted_num)
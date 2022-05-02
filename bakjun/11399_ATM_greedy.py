# 정렬해서 가장 빨리하는 사람부터 하면 됨

N = int(input())
arr = list(map(int,input().split()))

# N <=1000 이므로 counting 이용
count = [0]*(N+1)

for t in arr:
    count[t] += 1

multiple = N
result = 0
# 정렬한 후 첫번째 수는 N 번 더해짐
# 정렬한 후 k 번째 수는 N-(k-1) 번 더해짐
for num in range(N+1):
    if count[num] != 0:
        for cnt in range(count[num]):  # 해당 숫자 num이 존재하는 횟수
            result += (multiple-cnt)*num   # multiple - cnt 는 뒤에서부터 몇 번째 위치인지를 나타냄

        multiple -= count[num]  # 현재 센 것은 개수 빼주기

print(result)

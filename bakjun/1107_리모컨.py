N = int(input())
M = int(input())
not_working = list(map(int,input().split()))

move = [0,1,2,3,4,5,6,7,8,9]

for num in not_working:
    move.remove(num)

# 목표 채널 숫자가 하나라도 있다면 이동해볼 수 있다.


def can_go(channel):
    for char in str(channel):
        if int(char) in move:
            continue
        else:
            return False
    return True


INF = 0xffffffffff


result = abs(N-100)
new_result = INF
# 리모콘 숫자를 쓸 수 있는 경우
if move:
    # N 에 가장 가까운 곳으로 이동한다
    for i in range(result):
        if can_go(N+i):
            count = len(str(N+i))  # 리모컨 버튼 누른 횟수
            step = i               # N까지 가기위해 -  눌러야 하는 횟수
            new_result = count + i
            # new_result = min(result, new_result)
            break
        if N-i>=0 and can_go(N-i):
            count = len(str(N-i))  # 리모컨 버튼 누른 횟수
            step = i               # N까지 가기위해 +  눌러야 하는 횟수
            new_result = count + i
            # new_result = min(result, new_result)
            break


print(min(new_result, result))




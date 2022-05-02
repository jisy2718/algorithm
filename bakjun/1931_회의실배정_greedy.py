#---------------------------------시간초과---------------------------
# import sys
# input = sys.stdin.readline
# N = int(input())
#
# # 매 순간 시작할 수 있는 회의 중에, 끝나는 시간이 가장 짧은 것 선택
#
# L = []
# for _ in range(N):
#     meeting = list(map(int,input().split()))
#     L.append(meeting)
#
# L.sort(key=lambda x : ( x[1], x[0] ) ) # 뒷자리 작은 것부터 정렬하고, 값 같다면, 앞자리 작은 것부터 정렬
#
# result = 0
# start = 0
# # 이전 회의가 끝난 시간보다, 더 늦게 시작하는 회의 없는 경우 stop
# while L:
#     cs, ce = L.pop(0)
#     result += 1
#     si = 0  # 시작 index
#     for i in range(len(L)):
#         ns, ne = L[i]
#
#         # 시작시간(ns)가 이전회의 종료시간(ce)보다 같거나 커야함
#         if ns >= ce:
#             si = i
#             break
#     # 남은 회의들 중에서, 시작시간이, 이전 회의 종료시간보다 뒤에 있는 경우 없음
#     else:
#         L = []
#
#     L = L[si:]
#
# print(result)
#



#---------------------------------index만 이용하기------------------------------------------------
import sys
input = sys.stdin.readline
N = int(input())

# 매 순간 시작할 수 있는 회의 중에, 끝나는 시간이 가장 짧은 것 선택

L = []
for _ in range(N):
    meeting = list(map(int,input().split()))
    L.append(meeting)

L.sort(key=lambda x : ( x[1], x[0] ) ) # 뒷자리 작은 것부터 정렬하고, 값 같다면, 앞자리 작은 것부터 정렬

result = 0
start = 0
si = 0
# 이전 회의가 끝난 시간보다, 더 늦게 시작하는 회의 없는 경우 stop
while si != N:
    cs, ce = L[si]
    result += 1
    for i in range(si+1, len(L)):
        ns, ne = L[i]

        # 시작시간(ns)가 이전회의 종료시간(ce)보다 같거나 커야함
        if ns >= ce:
            si = i
            break
    # 남은 회의들 중에서, 시작시간이, 이전 회의 종료시간보다 뒤에 있는 경우 없음
    else:
        si = N



print(result)
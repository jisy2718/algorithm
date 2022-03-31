# 이진탐색에서 좌, 우측으로 번갈아가며 이동하면서 목표값 찾는 것 개수 세기
# 시작하자마자 찾는 것도 포함


def binary_search(left,right,target,from_lr):
    global cnt
    if left > right: # 찾는 수 없는 경우
        return

    mid = (left+right)//2
    if A[mid] == target:
        cnt += 1
    # 오른편 탐색
    elif A[mid] < target and from_lr in ['l','first']:
        binary_search(mid+1,right,target,'r')
    # 왼편 탐색
    elif A[mid] > target and from_lr in ['r', 'first']:
        binary_search(left,mid-1,target,'l')





T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    cnt = 0
    for target in B:
        binary_search(0,N-1,target,'first')
    print(f"#{tc} {cnt}")

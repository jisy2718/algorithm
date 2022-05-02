import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0216_input.txt", 'r')

alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

human_to_alien_map = {human_num : alien_num for human_num, alien_num in enumerate(alien)}
alien_to_human_map = {alien_num : human_num for human_num, alien_num in human_to_alien_map.items()}

print(f"human_to_alien_map {human_to_alien_map}")
print(f"alien_to_human_map {alien_to_human_map}")
from typing import List
def mergesort(lst:List[int]) -> List[int]:
    # base case
    if len(lst) <= 1:
        return lst
    # 좌우 나누기
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    # recursion
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left : List[int], right : List[int]) -> List[int]:
    l, r = 0, 0
    result = []
    # left, right 맨 앞 원소의 크기를 비교해서, 작은 것을 result에 넣어주기
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # 한 쪽이 바닥 나면 나머지를 result 뒤에 붙여줌
    result += left[l:] + right[r:]

    return result





# 외계어를 숫자로 변환

T = int(input())
for _ in range(1,T+1):
    # 1. input
    tc , N = input().split()
    N = int(N)

    arr = input().split()
    print(arr)

    # 2. alien_to_human_map
    for i in range(N):
        arr[i] = alien_to_human_map[arr[i]]

    # 3. arr 은 정수로 되어있으므로 정렬
    sorted_arr = mergesort(arr)

    # test
    for i in range(N-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            print("-----------------something wrong--------------------------")

    # 4. human_to_alien_map
    for i in range(N):
        sorted_arr[i] = human_to_alien_map[sorted_arr[i]]

    print(tc)

    print(*sorted_arr)

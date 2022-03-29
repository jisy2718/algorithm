arr = [2, 7, 3, 4, 5, 7]
N = 6


def make_perm(idx: int, used: list, perm: list):  # used : 사용한 index, perm : permutation list

    if idx == 6:  # 모든 idx에 대해서 들어갈 요소가 결정됨. 재귀 호출 하지 않음
        print(perm)
        return

    for i in range(N):  # i 번재 요소를 per[idx]에 넣어볼 건데..
        # i 번재 요소가 이전에 사용되었으면 사용하면 안됨
        if not used[i]:
            used[i] = 1
            perm[idx] = arr[i]
            make_perm(idx + 1, used, perm)
            used[i] = 0  # why? recursion에만 used를 업데이터 해서 넣어주고, 
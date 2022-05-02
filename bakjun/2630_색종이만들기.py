# 2차원 배열 lst의 모든 원소가 같은 값인지 판단하는 함수
def same(n,lst):
    if n == 1:
        return True
    else:
        start = lst[0][0]
        for i in range(n):
            for j in range(n):
                if start != lst[i][j]:
                    return False
    return True

# 2차원 배열 lst의 모든 원소가 같지 않다면, 4등분하는 함수
def divide(n, lst):
    global white_0
    global blue_1
    if same(n,lst):
        if lst[0][0] == 0:
            white_0 += 1
        else:
            blue_1 += 1
        return

    else:
        leftupper = [ [row[i] for i in range(n//2)]  for row in lst[:n//2] ]
        rightupper = [ [row[i] for i in range(n//2,n)] for row in lst[:n//2] ]
        leftlower = [ [row[i] for i in range(n//2)]  for row in lst[n//2:] ]
        rightlower = [[row[i] for i in range(n // 2, n)] for row in lst[n//2:]]

        divide(n//2,   leftupper)
        divide(n // 2, rightupper)
        divide(n // 2, leftlower)
        divide(n // 2, rightlower)


N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
white_0 = 0
blue_1= 0
divide(N, arr)
print(white_0)
print(blue_1)
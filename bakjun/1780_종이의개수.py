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

# 2차원 배열 lst의 모든 원소가 같지 않다면, 9등분하는 함수
def divide(n, lst):
    global minus
    global zero
    global plus

    if same(n,lst):
        if lst[0][0] == -1:
            minus += 1
        elif lst[0][0]==0:
            zero += 1
        else:
            plus += 1
        return

    else:
        leftupper = [ [row[i] for i in range(n//3)]  for row in lst[:n//3] ]
        midupper = [[row[i] for i in range(n//3, 2*n//3)] for row in lst[:n//3]  ]
        rightupper = [ [row[i] for i in range(2*n//3,n)] for row in lst[:n//3] ]

        leftcenter = [ [row[i] for i in range(n//3)] for row in lst[n//3 : 2*n//3] ]
        midcenter =  [[row[i] for i in range(n//3, 2*n//3)]  for row in lst[n//3 : 2*n//3] ]
        rightcenter = [[row[i] for i in range(2 * n // 3, n)] for row in lst[n//3 : 2*n//3] ]



        leftlower =  [ [row[i] for i in range(n//3) ] for row in lst[2 * n // 3:]]
        midlower =  [[row[i] for i in range(n//3, 2*n//3)]  for row in lst[2 * n // 3:]]
        rightlower = [[row[i] for i in range(2 * n//3, n)] for row in lst[2 * n // 3:]]

        divide(n // 3, leftupper)
        divide(n // 3, midupper)
        divide(n // 3, rightupper)
        divide(n // 3, leftcenter)
        divide(n // 3, midcenter)
        divide(n // 3, rightcenter)
        divide(n // 3, leftlower)
        divide(n // 3, midlower)
        divide(n // 3, rightlower)




N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
minus = 0
zero = 0
plus = 0
divide(N, arr)
print(minus)
print(zero)
print(plus)
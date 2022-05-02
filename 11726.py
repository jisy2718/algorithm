# 맨 오른쪽 (n번째) 것이 | 인 경우와 = 인경우로 나눠서 생각
# | 인경우는  n-1 번째 까지 둘 수 있는 경우의 수와 같음
# = 인 경우는 n-2 번째 까지 둘 수 있는 경우의 수와 같음
# f(0) = 1,f(1) = 1, f(2) = 2(= f(0) + f(1)), ...

N = int(input())
fibo =[0]*(N+1)
fibo[0] = 1
fibo[1] = 1
if N >=2:
    for i in range(2, N+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[N])
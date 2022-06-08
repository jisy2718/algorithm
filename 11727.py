n = int(input())

# f(0) = 1, f(1) = 1, f(2) = 2*f(0) + f(1), f(3) =  2*f(1) + f(2)

result = [0] * 1001
result[0] = result[1] = 1

for i in range(2,n+1):
    result[i] = result[i-1] + 2*result[i-2]
print(result[n]%10007)
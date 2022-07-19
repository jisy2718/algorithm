
def is_prime(n):
    if n == 1:
        return 0

    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            break
    else:
        return 1

    return 0

def find_prime(n):
    count = 0
    for i in range(n+1,2*n+1):
        count += is_prime(i)

    return count


while True:
    N = int(input())
    if N==0:
        break

    num = find_prime(N)
    print(num)
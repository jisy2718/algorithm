N = int(input())
def root(num):
    return int(num**(1/2))

def dfs(num,cnt):

    for n in range(root(num),0,-1):

        if n**2 == num:
            return cnt

        else:
            if cnt +1 <=4 :
                return dfs(num-n,cnt+1)

result = dfs(N,1)
print(result)

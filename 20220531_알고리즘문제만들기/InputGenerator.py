import random

for tc in range(50):
    # print(f'# {tc+1}')
    cnt = random.randrange(2, 5)
    number = random.randrange(1, 10000)
    case = str(number)
    for _ in range(cnt-1):
        num = random.randrange(1, 10000)
        number += num
        case += '+'+str(num)
    case += '='+str(number)
    print(case)
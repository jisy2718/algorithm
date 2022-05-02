T = int(input())
for _ in range(T):
    N = int(input())
    wave = [0] * (N + 1)

    if N == 3:
        print(1)
    elif N == 4 or N == 5:
        print(2)

    elif N >= 6:
        wave[1] = wave[2] = wave[3] = 1
        wave[4] = wave[5] = 2
        for i in range(6, N + 1):
            wave[i] = wave[i - 1] + wave[i - 5]
        print(wave[N])
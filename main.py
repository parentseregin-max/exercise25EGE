k = 0
for n in range(452_022, 10 ** 20):
    a = []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            if n // i != i:
                a.append(n // i)

    if a:
        M = min(a) + max(a)
        if M % 7 == 3:
            print(n, M)
            k += 1

    if k == 5:
        break

# 452025 150678
# 452029 23810
# 452034 226019
# 452048 226026
# 452062 226033
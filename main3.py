k = 0
for n in range(200_000_001, 10 ** 20):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)

    if len(a) >= 5:
        sort_a = sorted(a)
        M_n = sort_a[0] * sort_a[1] * sort_a[2] * sort_a[3] * sort_a[4]
        if 0 < M_n < n:
            print(M_n)
            k += 1

    if k == 5:
        break

# 1728
# 21632
# 1260
# 1152
# 4127787
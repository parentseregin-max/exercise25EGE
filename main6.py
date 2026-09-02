k = 0
for n in range(400_000_001, 10 ** 20):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)

    if len(a) >= 7:
        sort_a = sorted(a)
        D_n = sort_a[-7]
        if D_n > 0:
            print(D_n, len(a))
            k += 1

    if k == 5:
        break

# 34 10
# 2962963 14
# 1793722 30
# 21052632 62
# 754717 14
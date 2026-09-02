k = 0
for n in range(500_001, 10 ** 20):
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if (i % 10 == 8) and (i != 8):
                a.append(i)
            if (n // i % 10 == 8) and (n // i != 8):
                a.append(n // i)

    if a:
        print(n, min(a))
        k += 1

    if k == 5:
        break

# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348
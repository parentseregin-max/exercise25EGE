k = 0
answers = []
for n in range(1_200_000, 1, -1):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)

    if len(a) >= 3:
        sort_a = sorted(a)
        S = sort_a[-1] + sort_a[-2] + sort_a[-3]
        if (S % 2022 == 0) and (S != n):
            answers = [(n, S)] + answers
            k += 1

    if k == 5:
        break

for n, S in answers:
    print(n, S)

# 1091880 1182870
# 1116144 1209156
# 1140408 1235442
# 1164672 1261728
# 1188936 1288014
k = 0
answers = []
for n in range(1_200_200, 1, -1): # Все числа от 1_200_200 до 2 в порядке убывания
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)

    if len(a) >= 2:
        a_sort = sorted(a)
        S = a_sort[0] + a_sort[1]
        if S % 2022 == 0:
            answers = [(n, S)] + answers # Числа находятся в порядке убывания, используем спискок, чтобы перевернуть
            k += 1

    if k == 5:
        break

for n,S in answers:
    print(n, S)

# 1181459 4044
# 1182701 90990
# 1189499 20220
# 1192955 238596
# 1198487 8088

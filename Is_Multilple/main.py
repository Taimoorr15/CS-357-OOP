from is_multiple import Is_Multiple

a = Is_Multiple(20, 5)
print(a.check_multiple())   # 20 is a multiple of 5 (5 * 4)

b = Is_Multiple(21, 5)
print(b.check_multiple())   # 21 is not a multiple of 5

a.n = 25
print(a.check_multiple())   # 25 is not a multiple of 5

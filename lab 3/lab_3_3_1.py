def hofstadter_f_m(n: int) -> tuple:
    def F(n: int) -> int:
        return 1 if n == 0 else n - M(F(n - 1))

    def M(n: int) -> int:
        return 0 if n == 0 else n - F(M(n - 1))

    for i in range(n):
        yield (F(i), M(i))

n = int(input())
for item in hofstadter_f_m(n):
    print(item, end=' ')
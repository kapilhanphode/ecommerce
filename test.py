def test(n):
    if n == 0:
        return 1
    return n * test(n - 1)
print(test(3))
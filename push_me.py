def squares(n):
    for i in range(n):
        yield i ** 2

for square in squares(5):
    print(square)
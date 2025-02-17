def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


n = 10
for square in square_generator(n):
    print(square, end=" ")
#---------------------------------------
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("Enter a number: "))
print(",".join(even_numbers(n)))

#---------------------------------------
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = 50
print(list(divisible_by_3_and_4(n)))

#---------------------------------------
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


for sq in squares(3, 7):
    print(sq)

#---------------------------------------
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 10
for num in countdown(n):
    print(num, end=" ")

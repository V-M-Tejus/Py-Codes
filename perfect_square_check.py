def p_square(n):
    if n < 0:
        return False
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n


num = int(input("Enter a number: "))
if p_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")

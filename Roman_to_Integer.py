def R2I(rn):
    rdict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev = 0
    for i in rn[::-1]:
        value = rdict[i]
        if value > prev:
            result += value
        else:
            result -= value
        prev = value
    return result


print("Conversion")
a = input("Enter a number")
print("The Decimal Equivalent is ", R2I(a))

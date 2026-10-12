# extraction of digits using loops
n = int(input("Enter a number: "))
while n > 0:
    digit = n % 10
    print(digit)
    n //= 10
from math import sqrt
result = []
n = int(input("Enter a number: "))
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        result.append(i)
        if i != n // i:
            result.append(n // i)
print("Factors of", n, "are:", sorted(result))
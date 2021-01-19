number = int(input("Enter number: "))
result = 0

while number > 0:
    digit = number % 10
    result += digit
    number //= 10

print(result)
number = int(input("Enter number: "))
result = ""

while number > 0:
    digit = str(number % 10)
    result += digit
    number //= 10

print(result)

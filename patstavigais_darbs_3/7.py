start = int(input("Start: "))
end = int(input("End: "))
result = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        result += i

print(result)

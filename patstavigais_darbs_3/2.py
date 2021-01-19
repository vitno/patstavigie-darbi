start = int(input("Start: "))
end = int(input("End: "))
divider = int(input("Divider: "))
result = 0

for i in range(start, end + 1):
    if i % divider == 0:
        result += 1

print(f"{result} numbers between {start} and {end} can be divided by {divider}")
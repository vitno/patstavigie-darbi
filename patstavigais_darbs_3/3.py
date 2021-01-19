start = int(input("Start: "))
end = int(input("End: "))
result = 0

for i in range(start, end + 1):

    if i % 13 == 0 or (i % 4 != 0 and len(str(i)) == 3):
        continue
    elif i % 7000 == 0 and len(str(i)) == 4:
        break
    else:
        result += i

print(result)

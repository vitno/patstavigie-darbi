def triangle(rows):
    spaces = rows - 1
    result = ""

    for i in range(0, rows):

        for j in range(0, spaces):
            result += " "

        spaces -= 1

        for j in range(0, i + 1):
            result += "* "

        result += "\n"

    print(result)


triangle(int(input("Height: ")))
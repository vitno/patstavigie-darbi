height = int(input("Enter the height: "))
radius = int(input("Enter the radius: "))

base_area = 3.14 * radius ** 2

volume = base_area * height
area = 2 * base_area + ((2 * 3.14 * radius) * height)

print("Volume: " + str(volume))
print("Area: " + str(area))

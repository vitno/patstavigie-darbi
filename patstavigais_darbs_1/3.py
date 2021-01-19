seconds = int(input("Seconds: "))

minutes = seconds // 60
seconds = seconds % 60

hours = minutes // 60
minutes = minutes % 60

print(f"{hours} hours {minutes} minutes {seconds} seconds")

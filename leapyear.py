year = int(input("Enter:"))

if year % 4 == 0 and year % 100 != 0:
    print(year, "it is a leap year")
elif year % 100 == 0:
    print(year, "it is not a leap year")
elif year % 400 == 0:
    print(year, "it is a leap year")
else:
    print(year, "it is not a leap year")

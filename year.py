import sys

if len(sys.argv) == 2:
    year = int(sys.argv[1])
else:
    print("No input given - Using default value")
    year = 2027
is_leap = (year % 400 == 0) 

print("The year", year, "is a leap year:", is_leap)

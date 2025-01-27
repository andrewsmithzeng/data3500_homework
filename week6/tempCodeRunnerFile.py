total_miles = 0.0
total_gallons = 0.0

while True:
    gallons = float(input("Enter gallons used (-1 to end): "))
    if gallons == -1:
        break
    else:
        miles = float(input("Enter miles driven: "))
        mpg = miles / gallons
        print(f"The miles/gallon for this tank was {mpg:.6f}")
        total_miles += miles
        total_gallons += gallons

print(f"The overall average miles/gallon was {total_miles/total_gallons:.6f}")
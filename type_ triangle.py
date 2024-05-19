def triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Triangle is equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Triangle is isosceles"
    else:
        return "Triangle is scalene"

side1 = float(input('Type the side 1 value: '))   
side2 = float(input('Type the side 2 value: '))   
side3 = float(input('Type the side 3 value: '))   

result = triangle(side1, side2, side3)

print(result)
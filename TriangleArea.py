def triangleArea(height, width):
	area =(height * width) / 2
	return area


height = input("What is the height of your triangle?: ")
width = input("What is the width of your triangle?: ")

print("The area of your triangle is: " + str(triangleArea(int(width), int(height))))

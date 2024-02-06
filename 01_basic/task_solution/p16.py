# Input the coordinates of the left top corner and right bottom corner of the first rectangle
L1_x = int(input("Enter the x-coordinate of the left top corner of rectangle 1: "))
L1_y = int(input("Enter the y-coordinate of the left top corner of rectangle 1: "))
R1_x = int(input("Enter the x-coordinate of the right bottom corner of rectangle 1: "))
R1_y = int(input("Enter the y-coordinate of the right bottom corner of rectangle 1: "))

# Input the coordinates of the left top corner and right bottom corner of the second rectangle
L2_x = int(input("Enter the x-coordinate of the left top corner of rectangle 2: "))
L2_y = int(input("Enter the y-coordinate of the left top corner of rectangle 2: "))
R2_x = int(input("Enter the x-coordinate of the right bottom corner of rectangle 2: "))
R2_y = int(input("Enter the y-coordinate of the right bottom corner of rectangle 2: "))

# Check if the rectangles overlap
if L1_x >= R2_x or L2_x >= R1_x:
    overlap = False
elif L1_y <= R2_y or L2_y <= R1_y:
    overlap = False
else:
    overlap = True

# Print the result
if overlap:
    print("The rectangles overlap.")
else:
    print("The rectangles do not overlap.")

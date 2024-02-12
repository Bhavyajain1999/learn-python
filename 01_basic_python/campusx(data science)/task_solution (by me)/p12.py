import math

# Initialize the position
x = 0
y = 0

# Process input movements
while True:
    movement = input().strip().split()
    direction = movement[0]
    if direction == '!':
        break
    
    steps = int(movement[1])

    # Update the position based on the direction and steps
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# Compute the distance from the original point
distance = math.sqrt(x**2 + y**2)

# Print the distance
print(int(distance))

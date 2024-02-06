# Input hour and minute from the user
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

# Calculate the angle made by the hour hand with respect to 12:00
hour_angle = (hour % 12) * 30 + minute * 0.5


# Calculate the angle made by the minute hand with respect to 12:00
minute_angle = minute * 6


# Find the absolute difference between the two angles
angle_diff = abs(hour_angle - minute_angle)

# Calculate the smaller angle between the two possible angles
min_angle = min(angle_diff, 360 - angle_diff)

# Print the result
print(f"The minimum angle between hour and minute hand when the time is {hour}:{minute} is {min_angle} degrees.")

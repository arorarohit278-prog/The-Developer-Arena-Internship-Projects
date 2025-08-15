# Basic data processing script: Calculate average temperature

# Sample list of temperatures (in °C)
temperatures = [31.5, 32.0, 38.7, 25.2, 36.8]


# Calculate the average

average_temp = sum(temperatures) / len(temperatures)

# Display the result

print(f"Average Temperature: {average_temp:.2f}°C")

import matplotlib.pyplot as plt
from collections import deque

data_points = deque(maxlen=50)

# Create an empty plot
fig, ax = plt.subplots()
line, = ax.plot([])
# Set the x-axis and y-axis limits to 100
ax.set_xlim(2013, 2025)
ax.set_ylim(35_000, 75_000)

# Create a scatter plot to visualize the data points
scatter = ax.scatter([], [])
x_ = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y_ = [40_000, 42_000, 45_000, 50_000, 50_500, 60_000, 61_500, 70_000, 72_500]
# Iterate through the data points and update the scatter plot
for i in range(len(x_)):
	# Generate and add data points to the deque
	new_x = x_[i]
	new_y = y_[i]
	data_points.append((new_x, new_y))

	# Update the scatter plot with the new data points
	x_values = [x for x, y in data_points]
	y_values = [y for x, y in data_points]
	scatter.set_offsets(list(zip(x_values, y_values)))
	line.set_data(x_values, y_values)
	plt.pause(1)
# Save the animation as an animated GIF
plt.show()

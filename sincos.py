import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 2 * np.pi
num_points = 100

# Generate the x and y values for the sine wave
x_values = np.linspace(0, x_range, num_points)
y_sin = np.sin(x_values)

# Generate the x and y values for the cosine wave
y_cos = np.cos(x_values)

# Create line objects to plot the sine and cosine waves
line_sin, = ax.plot(x_values, y_sin, label='Sine')
line_cos, = ax.plot(x_values, y_cos, label='Cosine')

# Add a legend to the plot
ax.legend()

# Define the update function to animate the sine and cosine waves
def update(frame):
    # Generate new y values for the sine and cosine waves based on the current frame
    new_y_sin = np.sin(x_values + frame * 0.1)
    new_y_cos = np.cos(x_values + frame * 0.1)
    
    # Update the line objects with the new y values
    line_sin.set_ydata(new_y_sin)
    line_cos.set_ydata(new_y_cos)
    
    # Return the line objects for the animation to use
    return [line_sin, line_cos]

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=2000, interval=15)

# Display the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 2 * np.pi
num_points = 200

# Generate the x values for the step wave
x_values = np.linspace(0, x_range, num_points)

# Define the update function to animate the step wave
def update(frame):
    # Generate new y values for the step wave based on the current frame
    new_y_values = np.zeros_like(x_values)
    new_y_values[x_values + frame * 0.1 > np.pi] = 1
    
    # Plot the step wave
    ax.clear()
    ax.plot(x_values, new_y_values, 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(0, x_range)
    ax.set_ylim(-0.2, 1.2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Step Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=30, interval=10)

# Display the plot
plt.show()

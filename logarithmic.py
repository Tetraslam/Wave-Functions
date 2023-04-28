import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 10
num_points = 200

# Generate the x values for the logarithmic wave
x_values = np.linspace(0.01, x_range, num_points)

# Define the update function to animate the logarithmic wave
def update(frame):
    # Generate new y values for the logarithmic wave based on the current frame
    new_y_values = np.log10(1 + frame / 10) * np.sin(2 * np.pi * x_values)
    
    # Plot the logarithmic wave
    ax.clear()
    ax.plot(x_values, new_y_values, 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(0, x_range)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Logarithmic Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Display the plot
plt.show()

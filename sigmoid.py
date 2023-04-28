import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 10
num_points = 200

# Define the update function to animate the sigmoid wave
def update(frame):
    # Clear the plot
    ax.clear()
    
    # Generate the x values
    x_values = np.linspace(-x_range, x_range, num_points)
    
    # Generate new y values based on the current frame
    new_y_values = 1 / (1 + np.exp(-x_values + frame))
    
    # Plot the new wave
    ax.plot(x_values, new_y_values, 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(0, x_range)
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sigmoid Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=20, interval=50)

# Display the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 10
num_points = 200

# Generate the x values for the exponential wave
x_values = np.linspace(-x_range, x_range, num_points)

# Define the update function to animate the exponential wave
def update(frame):
    # Generate new y values for the exponential wave based on the current frame
    new_y_values = np.exp(-x_values*(1+frame/10))
    
    # Plot the exponential wave
    ax.clear()
    ax.plot(x_values, new_y_values, 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(0, x_range)
    ax.set_ylim(-0.2, 1.2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Exponential Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=100)

# Display the plot
plt.show()

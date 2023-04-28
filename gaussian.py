import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 25
num_points = 200

# Generate the x values for the Gaussian wave
x_values = np.linspace(-x_range, x_range, num_points)

# Define the update function to animate the Gaussian wave
def update(frame):
    # Generate new y values for the Gaussian wave based on the current frame
    new_y_values = np.exp(-x_values**2/(2*(1+frame/10)**2))
    
    # Plot the Gaussian wave
    ax.clear()
    ax.plot(x_values, new_y_values, 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(-x_range, x_range)
    ax.set_ylim(-0.2, 1.2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Gaussian Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=2000, interval=1)

# Display the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 10
num_points = 1000

# Define the update function to animate the Fourier wave
def update(frame):
    # Clear the plot
    ax.clear()
    
    # Generate the x values
    x_values = np.linspace(-x_range, x_range, num_points)
    
    # Generate the Fourier series by summing the first 10 odd harmonics
    fourier_sum = 0
    for n in range(1, 21, 2):
        fourier_sum += (4 / (n * np.pi)) * np.sin(n * x_values * np.pi / x_range) * np.exp(-1j * n * frame)
        time.sleep(0.01)
    
    # Plot the new wave
    ax.plot(x_values, np.real(fourier_sum), 'b-')
    
    # Set the plot limits and labels
    ax.set_xlim(-x_range, x_range)
    ax.set_ylim(-4, 4)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Continuous Fourier Wave')
    
    # Return the line object for the animation to use
    return ax.lines

# Set the animation interval and start the animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=10)

# Display the plot
plt.show()

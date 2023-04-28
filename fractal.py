import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import noise

fig, ax = plt.subplots()

# Set the x-axis range and the number of points to generate
x_range = 10
num_points = 10000

# Generate the x values
x_values = np.linspace(-x_range, x_range, num_points)

# Generate the Perlin noise values
noise_values = np.zeros(num_points)
for i, x in enumerate(x_values):
    noise_values[i] = noise.pnoise1(x / 5, octaves=6, persistence=0.5, lacunarity=2, repeat=1024, base=0)

# Plot the initial wave
ax.plot(x_values, noise_values, 'b-')

# Set the plot limits and labels
ax.set_xlim(-x_range, x_range)
ax.set_ylim(-2, 2)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Fractal Noise Wave')

# Define the update function to animate the fractal noise wave
def update(frame):
    # Do nothing
    pass

# Start the animation
ani = animation.FuncAnimation(fig, update, frames=lambda: iter([0]), interval=50)

# Display the plot
plt.show()

import numpy as np
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Setting up starting position
i = 0
j = 0
N = 1000  # Number of steps
point_p = []

# Set up plots, axes, title
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.grid(True, alpha=0.3)
ax.set_title('Random Walk')

# Define movement functions
def move_left(point_p):
    point_p[0] = point_p[0] - 1
    return point_p

def move_right(point_p):
    point_p[0] = point_p[0] + 1
    return point_p

def move_down(point_p):
    point_p[1] = point_p[1] - 1
    return point_p

def move_up(point_p):
    point_p[1] = point_p[1] + 1
    return point_p

# Generate random walk (INCLUDING STARTING POSITION)
current_position = [i, j]
point_p.append(current_position.copy())  # ✅ Add starting position (step 0)

for step in range(N):  # Run N times
    move_function = random.choice([move_left, move_right, move_down, move_up])
    current_position = move_function(current_position)
    point_p.append(current_position.copy())  # ✅ Add new position

# Convert to numpy array
new_array = np.array(point_p)

# Plot the complete path (trace)
ax.plot(new_array[:, 0], new_array[:, 1], 'b-', alpha=0.3, linewidth=1, label='Path')

# Scatter plot of all points (optional, shows visited positions)
ax.scatter(new_array[:, 0], new_array[:, 1], c='red', s=10, alpha=0.5, label='Visited points')

# Add the moving circle
graph = plt.Circle([new_array[0, 0], new_array[0, 1]], 0.5, fc='green', ec='darkgreen', alpha=0.8)
ax.add_patch(graph)
ax.legend()

# Print debug info
print(f"Total positions (including start): {new_array.shape[0]}")
print(f"Should be {N+1} positions")
print(f"First 5 positions:\n{new_array[:5]}")

# Animation function
def animate(frame):
    x = new_array[frame, 0]
    y = new_array[frame, 1]
    graph.center = (x, y)
    ax.set_title(f'Random Walk - Step {frame}/{len(new_array)-1}')
    return graph,

# Create animation
anim = animation.FuncAnimation(fig, animate, frames=len(new_array), interval=200, repeat=True)

# Save as GIF
writergif = animation.PillowWriter(fps=10)
anim.save('random_walk.gif', writer=writergif)
print("Animation saved as 'random_walk.gif'")

# Show the animation
plt.show()
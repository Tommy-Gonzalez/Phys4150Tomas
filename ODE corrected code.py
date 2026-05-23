import numpy as np
import matplotlib.pyplot as plt

# Variable declarations (NO units for numerical computation)
theta = 30 * np.pi/180
N = 1000
h = 0.01  # Increased from 0.0001 to see motion
v0 = 100.0  # m/s

# Initial conditions
x = 0.0
y = 0.0
x_velocity = v0 * np.cos(theta)
y_velocity = v0 * np.sin(theta)

# Physical parameters
m = 1.0  # kg
R = 0.08  # meters (8 cm)
rho = 1.22  # kg/m^3
C = 0.47  # Drag coefficient
g = 9.81  # m/s^2

# Pre-calculate drag constant
drag_constant = (np.pi * R**2 * rho * C) / (2 * m)

def ddt(all_variables, t):
    """Extract values from state vector and compute derivatives"""
    x, y, vx, vy = all_variables  # UNPACK the state vector
    
    # Calculate speed magnitude
    speed = np.sqrt(vx**2 + vy**2)
    
    # Derivatives
    dx_dt = vx
    dy_dt = vy
    dvx_dt = -drag_constant * vx * speed
    dvy_dt = -g - drag_constant * vy * speed
    
    return np.array([dx_dt, dy_dt, dvx_dt, dvy_dt])  # RETURN 4 values

# Storage arrays
all_positions = np.zeros((N+1, 4))  # Store all variables at each time
times = np.zeros(N+1)

# Initial state
all_variables = np.array([x, y, x_velocity, y_velocity])
all_positions[0] = all_variables
times[0] = 0

# Runge-Kutta Method
def runge_kutta(all_variables, times_array, N, h):
    for i in range(N):
        t = times_array[i]
        current_state = all_positions[i]  # Get state at current time
        
        # RK4 steps
        K1 = h * ddt(current_state, t)
        K2 = h * ddt(current_state + 0.5*K1, t + 0.5*h)
        K3 = h * ddt(current_state + 0.5*K2, t + 0.5*h)
        K4 = h * ddt(current_state + K3, t + h)
        
        # Update state
        next_state = current_state + (1/6)*(K1 + 2*K2 + 2*K3 + K4)
        all_positions[i+1] = next_state
        times_array[i+1] = t + h
    
    return all_positions, times_array

# Run the simulation
all_positions, times = runge_kutta(all_variables, times, N, h)

# Extract results for plotting
x_trajectory = all_positions[:, 0]
y_trajectory = all_positions[:, 1]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_trajectory, y_trajectory, 'b-', linewidth=2)
plt.scatter(x_trajectory[0], y_trajectory[0], color='green', s=100, label='Start')
plt.scatter(x_trajectory[-1], y_trajectory[-1], color='red', s=100, label='End')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Projectile Motion with Air Drag (RK4 Method)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.axis('equal')
plt.show()

print(f"Final position: x = {x_trajectory[-1]:.2f} m, y = {y_trajectory[-1]:.2f} m")
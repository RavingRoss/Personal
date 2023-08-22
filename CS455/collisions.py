import matplotlib.pyplot as plt
import numpy as np

# Define initial positions and velocities of the two particles
x1 = np.array([0.0, 0.0])  # initial position of particle 1
x2 = np.array([1.0, 0.0])  # initial position of particle 2
v1 = np.array([1.0, 0.0])  # initial velocity of particle 1
v2 = np.array([-1.0, 0.0]) # initial velocity of particle 2

# Defining the masses of the particles
m1 = 2
m2 = 1

# Define time step and simulation time
dt = 0.001  # time step
T = 2.0     # simulation time
n = int(T/dt)  # number of time steps

# Define coefficient of restitution
e = 1.0  # coefficient of restitution (elastic collision)

# Simulate the elastic collision of the two particles
x1_hist = np.zeros((n, 2))  # position history of particle 1
x2_hist = np.zeros((n, 2))  # position history of particle 2

for i in range(n):
    # Update positions of the two particles
    x1 = x1 + v1 * dt
    x2 = x2 + v2 * dt
    
    # Check if the two particles collide
    if np.linalg.norm(x2 - x1) < 0.05:
        # Calculate the normal and tangential vectors of the collision plane
        n = (x2 - x1) / np.linalg.norm(x2 - x1)
        t = np.array([-n[1], n[0]])
        
        # Calculate the velocities of the two particles in the collision plane
        v1n = np.dot(v1, n)
        v2n = np.dot(v2, n)
        
        # Calculate the velocities of the two particles after the collision in the collision plane
        v1n_new = (v1n * (m1 - e * m2) + 2 * e * m2 * v2n) / (m1 + m2)
        v2n_new = (v2n * (m2 - e * m1) + 2 * e * m1 * v1n) / (m1 + m2)
        
        # Calculate the velocities of the two particles after the collision in the tangential plane
        v1t = np.dot(v1, t)
        v2t = np.dot(v2, t)
        v1t_new = v1t
        v2t_new = v2t
        
        # Calculate the velocities of the two particles after the collision
        v1_new = v1n_new * n + v1t_new * t
        v2_new = v2n_new * n + v2t_new * t
        
        # Update velocities of the two particles
        v1 = v1_new
        v2 = v2_new
    
    # Save position history of the two particles
    x1_hist[i] = x1
    x2_hist[i] = x2

# Plot the positions of the two particles over time
plt.plot(x1_hist[:,0], x1_hist[:,1], 'r-', label='Particle 1')
plt.plot(x2_hist[:,0], x2_hist[:,1], 'b-', label='Particle 2')
plt.legend()
plt.show()
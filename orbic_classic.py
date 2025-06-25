import numpy as np
import matplotlib.pyplot as plt

def calculat_force(x, y):
    # Constants
    G = 6.67430e-11  # Gravitational constant
    m1 = 5.972e24   # Mass of Earth
    m2 = 1   # Mass in orbit (1 kg for simplicity)
    
    r = np.sqrt(x**2 + y**2)  # Distance from the center of Earth

    # Gravitational force calculation
    F = G * (m1 * m2)/(r**2)

    # Force components
    Fx = -F * (x / r)
    Fy = -F * (y / r)

    return Fx, Fy


def simulate_orbit(start_x, start_y, start_x_vel, start_y_vel, Time):
    
    poz_x = start_x
    poz_y = start_y
    vel_x = start_x_vel
    vel_y = start_y_vel

    end_x_log = []
    end_y_log = []

    steps_log = []

    m = 1


    

    #print(f"Simulation: {j}")
    
    poz_x = start_x
    poz_y = start_y
    vel_x = start_x_vel
    vel_y = start_y_vel

    steps = int(10**7)
    
    dt = Time / (steps)
    print(f"dt: {dt}")
    #print(f"i :{i}")
    for i in range(steps):
        poz_x += vel_x * dt
        poz_y += vel_y * dt

        Fx, Fy = calculat_force(poz_x, poz_y)

        vel_x += (Fx/m) * dt
        vel_y += (Fy/m) * dt

        #if i % 20 == 0:
        #    
        #    poz_x_log.append(poz_x)
        #    poz_y_log.append(poz_y)
        if i % 1000 == 0:
            
            end_x_log.append(poz_x)
            end_y_log.append(poz_y)
        
    return end_x_log, end_y_log
    

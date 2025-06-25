import orbic_classic
from matplotlib import pyplot as plt


x_log, y_log = orbic_classic.simulate_orbit(6370_000+100_000, 0, 0, 9600, 12000)

plt.plot(x_log, y_log, label='Orbit Path')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Orbit Simulation')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
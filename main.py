import orbic_classic
from matplotlib import pyplot as plt
import simulate_orbit
import time

start = time.perf_counter()
x_log, y_log = orbic_classic.simulate_orbit(6370_000 + 100_000, 0, 0, 9600, 12000)
#x_log, y_log = simulate_orbit.simulate_orbit(6370_000 + 100_000, 0, 0, 9600, 12000)
end = time.perf_counter()
print(f"python simulation completed in {end - start:.2f} seconds")

start = time.perf_counter()
#x_log, y_log = orbic_classic.simulate_orbit(6370_000 + 100_000, 0, 0, 9600, 12000)
x_log, y_log = simulate_orbit.simulate_orbit(6370_000 + 100_000, 0, 0, 9600, 12000)
end = time.perf_counter()


print(f"cpp simulation completed in {end - start:.2f} seconds")
plt.plot(x_log, y_log, label='Orbit Path')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Orbit Simulation')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
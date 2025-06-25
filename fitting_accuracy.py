import ogorki
from matplotlib import pyplot as plt
import infinity_principle

end_x_log, end_y_log, steps_log = ogorki.load_lists_from_pickle_with_steps('data_3600.pkl')

x, y = infinity_principle.cal_pos_with_infinity_principle(end_x_log[:], end_y_log[:], steps_log[:])

plt.scatter(x, y, s=0.2, color='red')

plt.scatter(end_x_log, end_y_log, s=0.2)

#plt.xlabel('Number of Steps')
#plt.ylabel('Distance along the line')
#plt.title('Orbital Simulation')
#plt.xlabel('X Position (m)')
#plt.ylabel('Y Position (m)')
#plt.axis('equal')
#plt.grid()

plt.show()
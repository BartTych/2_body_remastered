
import projection
import fit
import math
import matplotlib.pyplot as plt

def cal_pos_with_infinity_principle(xs, ys, dts):

    projections, m, base_x, base_y = projection.project_to_1d_along_line(xs, ys)
    projections_range = max(projections) - min(projections)
    dts_range = max(dts) - min(dts)
    dts = [x *(projections_range / dts_range) for x in dts]
    hiperbola = fit.fit_shifted_inverse_with_offset(projections, dts)
    
    print(hiperbola)    

    plt.plot(projections,dts)
    plt.scatter(projections, [hiperbola[0] / (x - hiperbola[1]) + hiperbola[2] for x in projections], label='Fitted Curve', color='red')
    plt.show()
    plt.cla()
    plt.clf()
    a, c, d = hiperbola

    # d to pozioma asymptota
    x, y = vector_from_magnitude_and_slope(c, m)

    print('test')
    return x + base_x, y + base_y


def vector_from_magnitude_and_slope(mag, slope):
    if math.isinf(slope):
        x = 0
        y = abs(mag) if slope > 0 else -abs(mag)
        # Reverse if mag is negative
        if mag < 0:
            y = -y
    else:
        # Base direction vector (1, slope)
        dx = 1
        dy = slope
        # Normalize
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        # Apply magnitude (including sign)
        x = dx * mag
        y = dy * mag
    return (x, y)

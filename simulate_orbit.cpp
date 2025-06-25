
#include <vector>
#include <cmath>
#include <tuple>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <utility>

std::pair<double, double> calculate_force(double x, double y) {
    // Constants
    const double G = 6.67430e-11;     // Gravitational constant
    const double m1 = 5.972e24;       // Mass of Earth
    const double m2 = 1.0;            // Mass of orbiting object

    double r = std::sqrt(x * x + y * y);  // Distance from Earth's center

    // Avoid division by zero
    if (r == 0.0) return {0.0, 0.0};

    double F = G * (m1 * m2) / (r * r);  // Gravitational force magnitude

    // Force components
    double Fx = -F * (x / r);
    double Fy = -F * (y / r);

    return {Fx, Fy};
}


std::tuple<std::vector<double>, std::vector<double>> simulate_orbit(
    double start_x, double start_y, double start_x_vel, double start_y_vel, double Time)
{
    std::vector<double> end_x_log;
    std::vector<double> end_y_log;
    std::vector<int> steps_log;

    double m = 1.0;
    
    int steps = static_cast<int>(1e7);
    double dt = Time / steps;

    double poz_x = start_x;
    double poz_y = start_y;
    double vel_x = start_x_vel;
    double vel_y = start_y_vel;

    for (int i = 0; i < steps; ++i) {
        poz_x += vel_x * dt;
        poz_y += vel_y * dt;

        auto [Fx, Fy] = calculate_force(poz_x, poz_y);

        vel_x += (Fx / m) * dt;
        vel_y += (Fy / m) * dt;
        if (i % 100 == 0) {
            end_x_log.push_back(poz_x);
            end_y_log.push_back(poz_y);
        }
    }
    
    

    return {end_x_log, end_y_log};
}


PYBIND11_MODULE(simulate_orbit, m) {
    m.def("simulate_orbit", &simulate_orbit, "Simulation of orbit",
          pybind11::arg("start_x"), pybind11::arg("start_y"),
          pybind11::arg("start_x_vel"), pybind11::arg("start_y_vel"),
          pybind11::arg("Time"));
    m.def("calculate_force", &calculate_force, "Calculate gravitational force",
          pybind11::arg("x"), pybind11::arg("y"));

}
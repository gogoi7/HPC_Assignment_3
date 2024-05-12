#include "utils.h"

int main() {
    std::vector<double> x_values;
    for (double x = 0.0; x <= 10.0; x += 0.2) {
        x_values.push_back(x);
    }

    //int n = 1000; // Fixed value of n

    for (double x : x_values) {
        double exact_value = besselJ0(x);
        int steps = 1000;//10 * std::pow(2, n);
        double approxtr = trapezoidRule(x, 0, M_PI, steps);
        double approxsr = simpsonsRule(x, 0, M_PI, steps);
        std::cout << "x: " << x << ", Trapezoid : " << approxtr << ", Simpsons: " << approxsr << " cyl_bessel : " << exact_value << std::endl;
    }

    return 0;
}

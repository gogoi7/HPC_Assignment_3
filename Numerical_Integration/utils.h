#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

// Function to compute J0(x) using library functions
double besselJ0(double x) {
    return std::cyl_bessel_j(0, x);
}

// Trapezoid rule for numerical integration
double trapezoidRule(double x, double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (std::cos(x*std::sin(a)) / M_PI + std::cos(x*std::sin(b)) / M_PI);
    for (int i = 1; i < n; ++i) {
        double xi = a + i * h;
        sum += std::cos(x*std::sin(xi)) / M_PI;
    }
    return h * sum;
}

// Simpson's rule for numerical integration
double simpsonsRule(double x, double a, double b, int n) {
    double h = (b - a) / n;
    double sum = std::cos(x*std::sin(a)) / M_PI + std::cos(x*std::sin(b)) / M_PI;
    for (int i = 1; i < n; ++i) {
        double xi = a + i * h;
        sum += (i % 2 == 0 ? 2 : 4) * std::cos(x*std::sin(xi)) / M_PI;
    }
    return h / 3.0 * sum;
}

// Function to compute relative error
double relativeError(double approx, double exact) {
    return std::abs((approx - exact) / exact);
}

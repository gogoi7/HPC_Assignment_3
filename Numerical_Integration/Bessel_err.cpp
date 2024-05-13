#include "utils.h"

int main() {
    double x_values[] = {3.83171}; // Add other x values as needed
    int n_values[] = {1, 2, 3, 4, 5, 6, 7, 8}; // n = 10 * 2^n

    std::ofstream outputFile("Bessel_err_cpp.txt"); // Replace "/path/to/output/file.txt" with the desired file path

    for (double x : x_values) {
        double exact_value = besselJ0(x);

        for (int n : n_values) {
            int steps = 10 * std::pow(2, n);
            double approxtr = trapezoidRule(x,0, M_PI, steps);
            double errortr = relativeError(approxtr, exact_value);
            double approxsr = simpsonsRule(x,0, M_PI, steps);
            double errorsr = relativeError(approxsr, exact_value);
            outputFile << steps << " " << errortr << " " << errorsr << std::endl;
        }
    }

    outputFile.close();

    return 0;
}

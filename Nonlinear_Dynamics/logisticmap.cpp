#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

class LogisticMap {
public:
    LogisticMap(double r) : r(r) {}
    
    double iterate(double x) {
        return r * x * (1 - x);
    }
    
private:
    double r;
};

int main() {
    const int n = 1000;
    const double x0 = 0.5;
    std::vector<double> rs(1000);
    std::vector<std::vector<double>> xn(n, std::vector<double>(1000));
    std::vector<double> lyapunovExponents(1000, 0.0); // Store the Lyapunov exponents

    for (int i = 0; i < 1000; i++) {
        rs[i] = 1.0 + i * (4.0 - 1.0) / (1000 - 1.0);
    }

    for (int i = 0; i < 1000; i++) {
        LogisticMap lmap(rs[i]);
        double x = x0;
        double sum = 0.0; // Accumulate the sum of the logarithmic differences
        for (int j = 0; j < n; j++) {
            double fx = lmap.iterate(x);
            double dfx = rs[i] * (1 - 2 * x); // Derivative of the logistic map
            if (std::abs(dfx) > 0.0) { // Check if derivative is non-zero
                sum += std::log(std::abs(dfx));
            }
            x = fx;
            xn[j][i] = x;
        }
        lyapunovExponents[i] = sum / n; // Calculate the average
    }

    std::ofstream rFile("r.txt");
    std::ofstream xFile("x.txt");
    std::ofstream lyapunovFile("lyapunov.txt"); // File to save the Lyapunov exponents

    for (int i = 500; i < n; i++) {
        for (int j = 0; j < 1000; j++) {
            rFile << rs[j] << " ";
            xFile << xn[i][j] << " ";
        }
        rFile << "\n";
        xFile << "\n";
    }

    for (int i = 0; i < 1000; i++) {
        lyapunovFile << rs[i] << " " << lyapunovExponents[i] << "\n"; // Save Lyapunov exponents
    }

    rFile.close();
    xFile.close();
    lyapunovFile.close();

    return 0;
}
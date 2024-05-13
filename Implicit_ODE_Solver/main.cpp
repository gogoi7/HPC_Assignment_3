#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

std::vector<double> backeuler(double y0, double ti, double tf, double dt) {
    int numSteps = static_cast<int>((tf - ti) / dt) + 1;
    std::vector<double> t(numSteps);
    std::vector<double> y(numSteps);
    
    t[0] = ti;
    y[0] = y0;
    
    for (int i = 1; i < numSteps; i++) {
        t[i] = t[i - 1] + dt;
        y[i] = y[i - 1] / (1 + dt);
    }
    
    return y;
}

std::vector<double> ts(double ti, double tf, double dt) {
    int numSteps = static_cast<int>((tf - ti) / dt) + 1;
    std::vector<double> t(numSteps);
    
    t[0] = ti;
    
    for (int i = 1; i < numSteps; i++) {
        t[i] = t[i - 1] + dt;
    }
    
    return t;
}


int main() {
    double y0 = 1.0; // initial value
    double ti = 0.0; // initial time
    double tf = 16.00001; // final time
    std::vector<int> n = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // values of n
    std::vector<double> dt_values(10); // time step values
    
    // Calculate dt values
    for (int i = 0; i < 10; i++) {
        dt_values[i] = 16.0 / std::pow(2, n[i]);
    }
    
    // Lists to store data
    std::vector<std::vector<double>> error_data;
    std::ofstream file("error_cpp.txt");

    for (int i = 0; i < 10; i++) {
        double dt = dt_values[i];
        std::vector<double> t, y;
        y = backeuler(y0, ti, tf, dt);
        t = ts(ti, tf, dt);
        
        double y_exact, error;
        
        for (int j = 1; j < t.size(); j++) {
            y_exact = std::exp(-t[j]);
            error = std::abs(y[j] - y_exact) / y_exact;
            file << t[j] << "," << error << "," << "dt = 16/2^" << n[i] << std::endl;
        }
        

    }
    
    
    file.close();
    
    return 0;
}



// #include <iostream>
// #include <cmath>

// double backwardEuler(double y0, double dt, int numSteps) {
//     double y = y0;
    
//     for (int i = 0; i < numSteps; i++) {
//         y = y / (1 + dt);
//     }
    
//     return y;
// }

// int main() {
//     double y0 = 1.0; // initial value
//     double dt = 0.1; // time step
//     int numSteps = 10; // number of steps
    
//     double result = backwardEuler(y0, dt, numSteps);
    
//     std::cout << "Result: " << result << std::endl;
    
//     return 0;
// }
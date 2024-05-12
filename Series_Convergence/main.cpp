#include "utils.h"

int main() {
    // Create an instance of HarmonicSeries
    HarmonicSeries harmonic_series;

    // Define the range of N values
    std::vector<int> N_range;
    for (int n = 0; n < 9; n++) {
        N_range.push_back(pow(2, n));
    }

    // Create empty vectors to store values
    std::vector<double> ascending_sums;
    std::vector<double> descending_sums;

    for (int N : N_range) {
        ascending_sums.push_back(harmonic_series.ascending_sum(N));
        descending_sums.push_back(harmonic_series.descending_sum(N));
    }

    // Calculate errors
    std::vector<double> asc_err;
    std::vector<double> des_err;
    double log2 = log(2);
    for (int i = 0; i < N_range.size(); i++) {
        asc_err.push_back(std::abs(ascending_sums[i] - log2));
        des_err.push_back(std::abs(descending_sums[i] - log2));
    }

    // Save the errors to a file for comparison
    std::ofstream file("errors_cpp.txt");
    if (file.is_open()) {
        file << "#N Ascending_Errors Descending_Errors\n";
        for (int i = 0; i < N_range.size(); i++) {
            file << N_range[i] << " " << asc_err[i] << " " << des_err[i] << "\n";
        }
        file.close();
    } else {
        std::cout << "Failed to open file for writing.\n";
    }

    return 0;
}

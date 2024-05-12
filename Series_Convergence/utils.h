#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

class HarmonicSeries {
public:
    /**
     * Calculate the sum of the harmonic series in ascending order.
     *
     * @param N The number of terms to sum.
     * @return The sum of the harmonic series.
     */
    double ascending_sum(int N) {
        double ascending_sum = 0;
        for (int n = 1; n <= N; n++) {
            ascending_sum += pow(-1, n + 1) / n;
        }
        return ascending_sum;
    }

    /**
     * Calculate the sum of the harmonic series in descending order.
     *
     * @param N The number of terms to sum.
     * @return The sum of the harmonic series.
     */
    double descending_sum(int N) {
        double descending_sum = 0;
        for (int n = N - 1; n > 0; n--) {
            descending_sum += pow(-1, n + 1) / n;
        }
        return descending_sum;
    }
};
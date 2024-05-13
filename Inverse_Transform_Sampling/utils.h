#include <vector>
#include <random>
#include <cmath>

// Inverse transform sampling function
std::vector<double> inverse_transform_sampling(int n, double gamma) {
    std::vector<double> samples;
    samples.reserve(n);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dis(0.0, 1.0);
    for (int i = 0; i < n; ++i) {
        double u = dis(gen);
        double x = gamma * tan(M_PI * (u - 0.5));
        samples.push_back(x);
    }
    return samples;
}

// Function to create histogram
std::vector<double> create_histogram(const std::vector<double>& samples) {
    const int num_bins = 102;
    const double min_value = -10.1;
    const double max_value = 10.1;
    std::vector<double> hist(num_bins, 0.0);
    double bin_width = (max_value - min_value) / num_bins;
    for (double sample : samples) {
        int bin_index = static_cast<int>((sample - min_value) / bin_width);
        if (bin_index >= 0 && bin_index < num_bins)
            hist[bin_index] += 1.0;
    }
    double total_samples = samples.size();
    for (double& bin_count : hist)
        bin_count /= (total_samples * bin_width);
    return hist;
}
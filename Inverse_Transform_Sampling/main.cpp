#include <iostream>
#include <fstream>
#include "utils.h"

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <n> <output_file>" << std::endl;
        return 1;
    }
    int n = std::stoi(argv[1]);
    std::string output_file = argv[2];
    double gamma = 1.0;
    std::vector<double> samples = inverse_transform_sampling(n, gamma);
    std::vector<double> hist = create_histogram(samples);
    std::ofstream outfile(output_file);
    if (outfile.is_open()) {
        outfile << "# bin_edges, counts" << std::endl;
        const int num_bins = 102;
        const double min_value = -10.1;
        const double max_value = 10.1;
        double bin_width = (max_value - min_value) / num_bins;
        for (int i = 0; i < num_bins; ++i) {
            double bin_start = min_value + i * bin_width;
            double bin_end = min_value + (i + 1) * bin_width;
            outfile << bin_start << " " << hist[i] << std::endl;
        }
        outfile.close();
    } else {
        std::cerr << "Unable to open output file" << std::endl;
        return 1;
    }
    return 0;
}

import sys
import matplotlib.pyplot as plt

infile = open(sys.argv[1], "r")
#outfile = sys.argv[2]
# Load data from the saved file
t = []
rel_err = []
labels = []

tmp1,tmp2,tmp3 = infile.readline().strip().split(",")
t.append(float(tmp1))
rel_err.append(float(tmp2))


for line in infile:
    time, error, label = line.strip().split(",")
    if label != tmp3:
        plt.plot(t, rel_err, label=tmp3,marker="o")
        t = []
        rel_err = []
    t.append(float(time))
    rel_err.append(float(error))
    tmp3 = label

plt.plot(t, rel_err, label=tmp3, marker="o")
plt.yscale("log")
plt.xlabel("Time")
plt.ylabel("Relative Error")
plt.title("Error of Backward Euler Method")
plt.grid()
plt.legend()
plt.show()
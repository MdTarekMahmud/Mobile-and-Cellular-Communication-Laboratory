import numpy as np
import matplotlib.pyplot as plt

# Base station positions
BS1 = np.array([0, 0])
BS2 = np.array([1000, 0])

# Mobile station position
MS = np.array([700, 300])

# Parameters
Pt = 30          # dBm
lam = 0.3        # wavelength in meter

# Calculate distances
d1 = np.linalg.norm(MS - BS1)
d2 = np.linalg.norm(MS - BS2)

# Free-space path loss
PL1 = 20*np.log10(4*np.pi*d1/lam)
PL2 = 20*np.log10(4*np.pi*d2/lam)

# Received power
Pr1 = Pt - PL1
Pr2 = Pt - PL2

print("Distance from BS1 =", round(d1,2), "m")
print("Distance from BS2 =", round(d2,2), "m")

print("Received Power from BS1 =", round(Pr1,2), "dBm")
print("Received Power from BS2 =", round(Pr2,2), "dBm")

# Select base station
if Pr1 > Pr2:
    selected = "BS1"
else:
    selected = "BS2"

print("Selected Base Station:", selected)

# Graph
plt.bar(["BS1", "BS2"], [Pr1, Pr2])
plt.xlabel("Base Station")
plt.ylabel("Received Power (dBm)")
plt.title("E6: Received Signal Strength-Based BS Selection")
plt.grid(axis="y")
plt.show()
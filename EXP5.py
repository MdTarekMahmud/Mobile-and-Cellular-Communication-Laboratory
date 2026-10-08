import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Base stations and cells
BS1, BS2 = np.array([0, 0]), np.array([1000, 0])
R = 500

# Mobile movement
x = np.arange(10, 991, 10)
y = np.zeros(len(x))

# Distance and received signal
d1 = np.abs(x - BS1[0])
d2 = np.abs(x - BS2[0])
P1 = -20*np.log10(d1)
P2 = -20*np.log10(d2)

# Serving BS and handover point
serve = np.where(P1 > P2, 1, 2)
h = np.where(np.diff(serve) != 0)[0][0] + 1
hx = x[h]

print(f"Handover occurs at x = {hx} m")
print("Handover: BS1 -> BS2")

# ------------------------------------------------
# Figure 1: Signal-strength graph
# ------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(x, P1, label="BS1 Signal", linewidth=2)
plt.plot(x, P2, label="BS2 Signal", linewidth=2)
plt.axvline(hx, linestyle="--", label="Handover")
plt.xlabel("Mobile Position (m)")
plt.ylabel("Received Signal Strength")
plt.title("E5: Handover Between Two Cellular Cells")
plt.legend()
plt.grid()
plt.show()

# ------------------------------------------------
# Figure 2: Two cells + moving mobile
# ------------------------------------------------
fig, ax = plt.subplots(figsize=(9,5))
ax.set_xlim(-600,1600)
ax.set_ylim(-600,600)
ax.set_aspect("equal")
ax.grid()

# Draw two cells
t = np.linspace(0, 2*np.pi, 7)
ax.plot(R*np.cos(t), R*np.sin(t), linewidth=2)
ax.plot(1000+R*np.cos(t), R*np.sin(t), linewidth=2)

# Base stations
ax.plot(0, 0, "^", markersize=12)
ax.plot(1000, 0, "^", markersize=12)

ax.text(-60, 60, "BS1")
ax.text(940, 60, "BS2")
ax.text(-250, -550, "CELL 1")
ax.text(750, -550, "CELL 2")

# Handover boundary
ax.axvline(hx, linestyle="--")
ax.text(hx-80, 450, "Handover")

# Mobile
mobile, = ax.plot([], [], "o", markersize=10)
status = ax.text(-500, 500, "")

def update(i):
    mobile.set_data([x[i]], [y[i]])

    if i < h:
        status.set_text("Serving BS: BS1")
    else:
        status.set_text("HANDOVER: BS1 -> BS2")

    return mobile, status

ani = FuncAnimation(fig, update, frames=len(x),
                    interval=40, repeat=False)

plt.xlabel("Distance (m)")
plt.ylabel("Distance (m)")
plt.title("Two-Cell Handover Simulation")
plt.show()
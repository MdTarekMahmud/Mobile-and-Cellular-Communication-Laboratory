import numpy as np
import matplotlib.pyplot as plt

def erlang_b(A, N):
    B = 1.0
    for k in range(1, N + 1):
        B = A * B / (k + A * B)
    return B


# Parameters
holding_time, arrival_rate, GOS = 2.5, 2, 0.02

traffic = arrival_rate * holding_time
channels = np.arange(1, 21)


# Calculations
blocking = np.array([erlang_b(traffic, N) for N in channels])
carried = traffic * (1 - blocking)

N_needed = channels[blocking <= GOS][0]


print(f"Traffic Intensity = {traffic} Erlangs | "
      f"Channels needed for {GOS*100:.0f}% GOS = {N_needed}")

print("Channels  Carried(Erl)  Blocking(%)")

for N, C, B in zip(channels, carried, blocking):
    print(f"{N:8d}  {C:12.3f}  {B*100:11.3f}")


# ---------------- GRAPHS ----------------

plt.figure(figsize=(11, 8))


# Graph 1
plt.subplot(2, 2, 1)

plt.plot(channels, carried, 'o-', label='Carried')
plt.axhline(traffic, color='r', linestyle='--', label='Offered')

plt.title("Carried Traffic vs Channels")
plt.xlabel("Channels")
plt.ylabel("Erlangs")

plt.grid(True)
plt.legend()


# Graph 2
plt.subplot(2, 2, 2)

plt.plot(channels, blocking * 100, 'o-')
plt.axhline(GOS * 100, color='r', linestyle='--', label='GOS target')

plt.title("Blocking vs Channels")
plt.xlabel("Channels")
plt.ylabel("Blocking (%)")

plt.grid(True)
plt.legend()


# Graph 3
rates = np.arange(1, 11)

plt.subplot(2, 2, 3)

plt.plot(rates, rates * holding_time, 'o-')

plt.title("Traffic vs Arrival Rate")
plt.xlabel("Calls/min")
plt.ylabel("Erlangs")

plt.grid(True)


# Graph 4
loads = np.arange(1, 21)

plt.subplot(2, 2, 4)

for N in [5, 10, 15, 20]:
    plt.plot(
        loads,
        [erlang_b(A, N) * 100 for A in loads],
        label=f'{N} ch'
    )

plt.title("Blocking vs Traffic Load")
plt.xlabel("Erlangs")
plt.ylabel("Blocking (%)")

plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()
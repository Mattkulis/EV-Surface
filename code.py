import numpy as np
import matplotlib.pyplot as plt

# Fixed loss per trade
L = 0.5

# Range of returns
R = np.linspace(0.1, 2.0, 100)

# Minimum probability to be profitable
p_min = L / (R + L)

# Plot
plt.figure(figsize=(8,5))
plt.plot(R, p_min, label=f'Loss = {L*100:.0f}%')
plt.xlabel('Minimum Return per Trade (R)')
plt.ylabel('Minimum Probability of Win (p)')
plt.title('Minimum Win Probability vs Minimum Return for Positive EV')
plt.grid(True)
plt.legend()
plt.show()

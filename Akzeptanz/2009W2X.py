import numpy as np
import matplotlib.pyplot as plt


Threshold_values = [1.0, 1.01, 1.02, 1.05, 1.1, 1.125, 1.15, 1.2, 1.3, 1.5]
events = [1775600, 1558700, 1364597, 922474, 542617, 451770, 394950, 333149, 279156, 229596]
Scaling_parameter = 17756
events_scaled = [x / Scaling_parameter for x in events]

plt.plot(Threshold_values, events_scaled, 'x-b')
plt.xlabel('Threshold $T_{RICH}$')
plt.ylabel('Relative Akzeptanz [%]')
plt.grid(True)
plt.title('2009W2X data')
plt.show()

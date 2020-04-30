import numpy as np
import matplotlib.pyplot as plt


Threshold_values = [1.0, 1.01, 1.02, 1.05, 1.1, 1.125, 1.15, 1.2, 1.3, 1.5]
events = [10163830, 9148748, 8196452, 5782136, 3231271, 2506339, 2026971, 1505625, 1142913, 920855]
Scaling_parameter = 101638.3
events_scaled = [x / Scaling_parameter for x in events]

plt.plot(Threshold_values, events_scaled, 'x-b')
plt.xlabel('Threshold $T_{RICH}$')
plt.ylabel('Relative Akzeptanz [%]')
plt.grid(True)
plt.title('2008 data')
plt.show()

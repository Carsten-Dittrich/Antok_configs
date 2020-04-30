import numpy as np
import matplotlib.pyplot as plt


Threshold_values = [1.0, 1.01, 1.02, 1.05, 1.1, 1.125, 1.15, 1.2, 1.3, 1.5]
events = [12347770, 10979670, 9723534, 6669492, 3679236, 2877914, 2358247, 1795369, 1378254, 1080498]
Scaling_parameter = 123477.7
events_scaled = [x / Scaling_parameter for x in events]

plt.plot(Threshold_values, events_scaled, 'x-b')
plt.xlabel('Threshold $T_{RICH}$')
plt.ylabel('Relative Akzeptanz [%]')
plt.show()
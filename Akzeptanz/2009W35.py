import numpy as np
import matplotlib.pyplot as plt


Threshold_values = [1.0, 1.01, 1.02, 1.05, 1.1, 1.125, 1.15, 1.2, 1.3, 1.5]
events = [3590226, 3144859, 2751255, 1859357, 1102702, 923699, 811119, 687441, 577323, 473049]
Scaling_parameter = 35902.26
events_scaled = [x / Scaling_parameter for x in events]

plt.plot(Threshold_values, events_scaled, 'x-b')
plt.xlabel('Threshold $T_{RICH}$')
plt.ylabel('Relative Akzeptanz [%]')
plt.grid(True)
plt.title('2009W35 data')
plt.show()

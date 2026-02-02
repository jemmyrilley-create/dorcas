# simulation of a capacitor in an RC circuit
import numpy as np
import matplotlib.pyplot as plt
R = 1000  # resistance in ohms
C = 1e-6  # capacitance in farads
V0 = 5    # initial voltage across the capacitor in volts

t = np.linspace(0, 0.01, 1000)  # time from 0 to 10 ms
Vc = V0 * np.exp(-t / (R * C))  # voltage

plt.plot(t, Vc)
plt.title('Discharge of a Capacitor in an RC Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Voltage across Capacitor (V)')
plt.grid()
plt.show()

#discharge of capacitor simulation complete
#Vc(t)= V0 * exp(-t/(R*C))

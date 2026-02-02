# Temparute graph
import random, time
import matplotlib.pyplot as plt

temp = []
for t in range(10):
    temp = 25 + random.uniform(-5.0, 5.0)
    temp.append(temp)
    with open("temperature_log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, {temp:.2f}\n")
    time.sleep(1)


plt.plot(temp)
plt.title("Temperature Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.savefig("temperature_plot.png")
plt.show()
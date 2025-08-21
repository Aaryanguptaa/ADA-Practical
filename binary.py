import matplotlib.pyplot as plt

elements = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
times = [4.876600e-08, 4.934900e-08, 4.974400e-08, 6.027200e-08, 3.595500e-08, 6.230600e-08, 2.932600e-08, 4.510500e-08]

plt.plot(elements, times, marker='o', color='blue', label='Binary Search Time')
plt.xlabel('Number of Elements')
plt.ylabel('Time per Search (seconds)')
plt.title('Binary Search Time vs Number of Elements')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

elements = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
times = [
    3.484700e-07,
    6.400580e-07,
    8.705900e-07,
    4.788549e-06,
    7.649380e-07,
    1.143279e-05,
    8.978423e-06,
    9.783208e-05
]

plt.plot(elements, times, marker='o', color='blue', label='Linear Search Time')
plt.xlabel('Number of Elements')
plt.ylabel('Time per Search (seconds)')
plt.title('Linear Search Time vs Number of Elements')
plt.grid(True)
plt.legend()
plt.show()



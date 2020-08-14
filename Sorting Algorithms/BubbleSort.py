import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Bubble Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = np.random.randint(100, size=(100))
bars = ax.bar(range(len(array)), array, color='black')

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                yield array

def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=bubbleSort(array), interval=1,
    repeat=False)
plt.show()

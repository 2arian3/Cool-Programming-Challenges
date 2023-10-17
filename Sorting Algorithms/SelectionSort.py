import matplotlib.pyplot as plt
import matplotlib.animation as an
from DatasetGenerator import get_dataset

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Selection Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = get_dataset()
bars = ax.bar(range(len(array)), array, color='black')

def selectionSort(array):
    for i in range(len(array)):
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
    fargs=(bars, ), frames=selectionSort(array), interval=1,
    repeat=False)
plt.show()

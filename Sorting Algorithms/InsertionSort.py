import matplotlib.pyplot as plt
import matplotlib.animation as an
from DatasetGenerator import get_dataset

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Insertion Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = get_dataset()
bars = ax.bar(range(len(array)), array, color='black')

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and  array[j] > key:
            array[j+1] = array[j]
            j -= 1
            yield array
        array[j+1] = key 

def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=insertionSort(array), interval=1,
    repeat=False)
plt.show()

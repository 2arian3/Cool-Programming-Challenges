import matplotlib.pyplot as plt
import matplotlib.animation as an
from DatasetGenerator import get_dataset

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Quick Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = get_dataset()
bars = ax.bar(range(len(array)), array, color='black')

def quickSort(array, start, end):
    if end <= start:
        yield array
        return
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            yield array
    i += 1
    array[i], array[end] = array[end], array[i]
    yield from quickSort(array, start, i - 1)
    yield from quickSort(array, i + 1, end)

def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=quickSort(array, 0, len(array)-1), interval=1,
    repeat=False)
plt.show()

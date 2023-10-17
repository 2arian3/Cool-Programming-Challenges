import matplotlib.pyplot as plt
import matplotlib.animation as an
from DatasetGenerator import get_dataset

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Heap Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = get_dataset()
bars = ax.bar(range(len(array)), array, color='black')

def max_heapify(array, i, size):
    left, right = 2 * (i+1) - 1, 2 * (i+1)
    largest = i
    if left < size and array[i] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        max_heapify(array, largest, size)       

def build_max_heap(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        max_heapify(array, i, n)
    
def heap_sort(array):
    n = len(array)
    build_max_heap(array)
    for i in range(n, 1, -1):
        n -= 1
        array[i-1], array[0] = array[0], array[i-1]
        yield array
        max_heapify(array, 0, n)

def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=heap_sort(array), interval=1,
    repeat=False)
plt.show()

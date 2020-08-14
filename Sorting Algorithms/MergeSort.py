import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Bubble Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = np.random.randint(100, size=(100))
bars = ax.bar(range(len(array)), array, color='black')

def merge(A, start, mid, end):
    merged = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if array[left] < array[right]:
            merged.append(array[left])
            left += 1
        else:
            merged.append(array[right])
            right += 1

    while left <= mid:
        merged.append(array[left])
        left += 1

    while right <= end:
        merged.append(array[right])
        right += 1

    for i, num in enumerate(merged):
        array[start + i] = num
        yield array

def mergeSort(array, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(array, start, mid)
    yield from mergeSort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array
      
def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=mergeSort(array, 0, len(array)-1), interval=1,
    repeat=False)
plt.show()
print(array)

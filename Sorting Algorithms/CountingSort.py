import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np

swaps = 0
fig, ax = plt.subplots()
ax.set_title('Counting Sort')
numberOfSwaps = ax.text(0.01, 0.95, "", transform=ax.transAxes)
array = np.random.randint(100, size=(100))
bars = ax.bar(range(len(array)), array, color='black')

def countingSort(array):
    temp = array.copy()
    counter = [0] * (max(array) + 1)
    for number in array:
        counter[number] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]  
    for number in temp:
        array[counter[number]-1] = number
        counter[number] -= 1
        yield array             

def update(array, bars):
    global swaps
    for bar, val in zip(bars, array):
        bar.set_height(val)
    swaps += 1
    numberOfSwaps.set_text("Swaps: {}".format(swaps))
    
anim = an.FuncAnimation(fig, func=update,
    fargs=(bars, ), frames=countingSort(array), interval=1,
    repeat=False)
plt.show()

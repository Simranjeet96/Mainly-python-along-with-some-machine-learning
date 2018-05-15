# import matplotlib.pyplot as plt
# import numpy as np

# # Simple data to display in various forms
# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# fig = plt.figure(figsize=(6,6), facecolor='white')

# # New axis over the whole figure, no frame and a 1:1 aspect ratio
# ax = fig.add_axes([0,0,2,2], frameon=True, aspect=1)

# # Just a figure and one subplot
# # f, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')




# plt.show()
import numpy as np
import matplotlib.pyplot as plt

freq = 100 
def sine(x, phase=0, freq=freq):
    return np.sin((freq * x + phase))

dist = np.linspace(-0.5,0.5,256)
x,y = np.meshgrid(dist, dist)
grid = (x**2+y**2)

testpattern = sine(grid, freq=freq)
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

fig, axes = plt.subplots(3, 6, figsize=(96, 48))
fig.subplots_adjust(hspace=0.3, wspace=0.05)

for ax, interp_method in zip(axes.flat, methods):
    ax.imshow(testpattern , interpolation=interp_method, cmap='gray')
    ax.set_title(interp_method)

plt.show()


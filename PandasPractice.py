import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Slider

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
sample_size = 10000
normal = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
gamma = np.random.gamma(shape = 1.0, scale=1.0, size=sample_size)
uniform = np.random.uniform(low=0.0, high=10.0, size=sample_size)
exponential = np.random.exponential(scale=1.0, size=sample_size)

fig, sub_plt = plt.subplots()
plt.subplots_adjust(top=0.65) # Adjust subplot to not overlap with radio box

axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.7, 0.25, 0.25], facecolor=axcolor)
radio = RadioButtons(rax, ('Normal', 'Gamma', 'Uniform', 'Exponential'))

def dist_func(type_l):
    sub_plt.clear() # comment this line if you want to keep previous drawings
    dist_dict = {'Normal':normal, 'Gamma':gamma, 'Uniform':uniform, 'Exponential':exponential}
    data_type = dist_dict[type_l]
    hist = sub_plt.hist(data_type,bins=100)
    plt.draw()

radio.on_clicked(dist_func)
plt.show()
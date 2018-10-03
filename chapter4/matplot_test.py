#matplotのテスト

import math
from matplotlib import pyplot
import numpy as np

pi = math.pi

x = np.linspace(0, 2*pi, 100)
y = np.sin(x)

pyplot.plot(x, y)

pyplot.show()
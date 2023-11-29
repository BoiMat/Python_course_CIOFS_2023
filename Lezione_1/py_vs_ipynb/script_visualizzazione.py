# File .py (script.py) - Esempio con grafico Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Grafico di sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
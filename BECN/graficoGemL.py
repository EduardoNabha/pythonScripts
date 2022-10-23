import matplotlib.pyplot as plt
import numpy as np
import math


#GRÁFICO DE gXl
gravidade = [9.75,9.82,9.88,9.77,9.60,9.69,9.73,9.12,9.46,9.47]
#l em cm
l = [0.80,0.74,0.68,0.5,0.45,0.39,0.32,0.25,0.19,0.13]

plt.plot(l,gravidade, marker='o',label='g=(2π/T)²L\n')
plt.xlabel('L(centímetros)')
plt.ylabel('Gravidade(m/s²)')
plt.title('G em função de L')
plt.legend()
plt.yticks(range(0,20,1))
#plt.xticks(range(0,1.1,0.1))


plt.show()

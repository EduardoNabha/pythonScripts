import matplotlib.pyplot as plt
import numpy as np
import math

#constante
gravidade = 9.8

#EIXO X
#x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5,
#8, 8.5, 9, 9.5, 10]

x = np.arange(start=0, stop= 10.5, step=1)
y = []
#y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(x)):
    y.append(2*math.pi*(math.sqrt(x[i]/gravidade)))
#    print(y[i])

#PLOTANDO O GRÁFICO
plt.plot(x,y, marker='o', label='T = 2π√(L/g)\ng ≅ 9.8')

plt.xlabel('L(centímetros)')
plt.ylabel('T(oscilações)')
plt.title('T em função de L')
plt.yticks(range(0,11,1))
plt.xticks(range(0,11,1))
plt.legend()
plt.show()


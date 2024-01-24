import numpy as np
import matplotlib.pyplot as plt
from Ex_1 import edo, y_barra, y_linha

def Erro(exata,funcao, N, t_i, t_f, val_i):
    B  = np.zeros((4,N))
    dt = []
    for j in range(1,N+1):
        dt.append((t_f - t_i)/(j))
        for i in range(4):
            a         = edo(funcao, j+1, t_i, t_f, val_i, i)
            B[i][j-1] = 100*np.abs((a[1][-1] - exata(a[0])[-1])/exata(a[0])[-1])
    plt.plot(dt,B[0], label = 'Explícito')
    plt.plot(dt,B[1], label = 'Implícito')
    plt.plot(dt,B[2], label = 'Rk2')
    plt.plot(dt,B[3], label = 'Rk4')
    plt.xscale('log')
    plt.title('Erro relativo para diferentes passos de tempo')
    plt.xlabel("Passo de tempo (dt)")
    plt.ylabel("Erro relativo (%)")
    plt.legend()
    plt.gca().invert_xaxis()
    plt.show()

Erro(y_barra, y_linha, 100, 0, 1, 1)  
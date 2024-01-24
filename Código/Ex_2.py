import numpy as np
import matplotlib.pyplot as plt

def y_linha(t,y):
    return 1 + (y/t)

def y_barra(t):
    return t*np.log(t) + 2*t


def edo(funcao, N, t_i, t_f, val_i, tipo):
    t       = np.linspace(t_i, t_f, N)
    dt      = (t_f - t_i)/(N-1)
    y       = np.zeros(len(t))
    y[0]    = val_i

    if tipo == 0:
        for k in range(1, len(t)):
            y[k] = y[k-1] + dt*funcao(t[k-1], y[k-1])
        tipo = 'Exp'

    elif tipo == 1:
        for k in range(1, len(t)):
            y[k] = (y[k-1] + dt)/(1 - dt/t[k])
        tipo = 'Imp'
    
    elif tipo == 2:
        for k in range(1, len(t)):
            k1   = dt*funcao(t[k-1], y[k-1])
            k2   = dt*funcao(t[k-1] + dt, y[k-1] + k1)
            y[k] = y[k-1] + 0.5*(k1 + k2)
        tipo = 'Rk2'

    elif tipo == 3:
        for k in range(1, len(t)):
            k1   = dt*funcao(t[k-1], y[k-1])
            k2   = dt*funcao(t[k-1] + dt*0.5, y[k-1] + 0.5*k1)
            k3   = dt*funcao(t[k-1] + dt*0.5, y[k-1] + 0.5*k2)
            k4   = dt*funcao(t[k-1] + dt, y[k-1] + k3)
            y[k] = y[k-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        tipo = 'Rk4'

    return t, y, tipo


def compara(exata,funcao, N, t_i, t_f, val_i):
    A = np.zeros((5,N))
    B = np.zeros((4,N))
    tipos = []

    for i in range(4):
        a = edo(funcao, N, t_i, t_f, val_i, i)
        A[i]  =  a[1]
        A[-1] =  a[0]
        plt.plot(A[-1], A[i], '--', label = f'{a[2]}')
        tipos.append(a[2])
    y_  = exata(A[-1])
    plt.plot(A[-1], y_, label = 'Exato')
    plt.title('Comparação entre métodos')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()


compara(y_barra,y_linha, 50, 1, 2, 2)
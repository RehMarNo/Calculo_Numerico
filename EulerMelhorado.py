#Metódo de Euler Melhorado
import numpy as np

def eulerMod(h, Tmax):
  u = 8       #condição inicial
  itMax = Tmax/h     #quantidade máxima de iterações
  for i in np.arange(1,itMax):
    t = (i-1)*h
    k1 = (-0.5*u + 2 + t)    #edo
    u_Atualizado = u + h*k1
    k2 = (-0.5*u_Atualizado + 2 + t + h)
    u= u + h * (k1 + k2)/2
    print("it: ", i, "|  u[i]: ",u)

eulerMod(np.exp(-2),1)

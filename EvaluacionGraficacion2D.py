# Importamr librerias
import numpy as np
import matplotlib.pyplot as plt

# Crear ventana
plt.axis()  # Se ajusta al tamanio necesario
plt.axis()  # muestra los numeros de los ejes x,y (aunque no tenga nada escrito)
plt.grid()  # muestra las lineas cuadriculadas (aunque no tenga nada escrito)

# Crear centro
r=5*5
Rz=4*6
Sx=5/5
Sy=4/5

xc=Sx
yc=Sy

# Crear ciculo 
p1 = 0 * np.pi/180 
p2 = 360 * np.pi/180
dp=(p2 - p1)/180

xlast = xc+r*np.cos(p1)
ylast = yc+r*np.sin(p2)

# Imprimir circulo
for p in np.arange(p1, p2+dp, dp):
    xp = xc+r*np.cos(p)
    yp = yc+r*np.sin(p)
    plt.plot([xlast, xp],[ylast, yp], c=(.8, 0, .8), linewidth=2)
    xlast = xp
    ylast = yp

#CERAR CUADRADO DEL CICULO
xt = xc-2*r
xu = xt+4*r
yt = yc+r
yu = yt-2*r

plt.plot([xt,xt],[yt,yu],c='orange')
plt.plot([xu,xu],[yt,yu],c='orange')
plt.plot([xt,xu],[yt,yt],c='orange')
plt.plot([xt,xu],[yu,yu],c='orange')

#CREAR SEGUNDO CUADRADO
xrec=np.array([xc,xc,xc+4*r,xc+4*r,xc])
yrec=np.array([yc,yc-2*r,yc-2*r,yc,yc])
plt.plot(xrec,yrec, color='k')

plt.gca().set_aspect('equal')
plt.show()
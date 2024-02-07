
# 'w' borrar todo el contenido del archivo
""" import re
#file_x = open('eje1.txt', 'w')
#file_x.close()
# Se recominda abrir los archivos con "with" para evitar olvidar cerrar los mismos
archivo = 'eje1.txt'

with open(archivo) as f:
    for line in f:
        print('*****')
        # Separar string por espacios en blanco
        x = line.split()
        print(x)
print('$$$$$$$$$$$$$$$$$$$$$$')


contador = 0      
with open(archivo) as f:
    for line in f:
        # Buscar por parámetro regex por linea
        if re.match("^H", line):
            contador += 1
    
print(contador)

import csv """

""" with open(archivo) as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print(date, symbol, closing_price) """
        
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = x*np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()
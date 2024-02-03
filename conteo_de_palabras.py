import sys
from collections import Counter

# Cuenta el número de veces que se repite las palabras
# recibe como parámetro el número de palabras que se desee mostrar
# Ejemplo de ejecución:
# $cat ejemplo.txt | conteo_de_palabras.py <"numero que desea mostrar">
try:
    #  Convierte en entero el parámetro que se ingreso previmamente
    num_words = int(sys.argv[1])
except:
    print("usage: conteo_de_palabras.py num_words")
    sys.exit(1)   # muestra el error en caso de no ingresar un número como parámetro

counter = Counter(word.lower()                      
                  for line in sys.stdin
                    for word in line.strip().split()  
                        if word)    
for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")



def get_domain(email: str) -> str:
    # El separador que se utilizará para este ejercicio será @
    # Se ultiza el  [-1] para tomar el ultimo valor de la lista al realizar la separación
    # Utilizamos lower para convertir todo en minúsculas
    return email.lower().split("@")[-1]


print(get_domain('alvarof808@gmail.com'))


assert get_domain('alvarof808@gmail.com') == 'gmail.com'
archivo = 'eje1.txt'
from collections import Counter

with open(archivo, 'r') as f:
    contador = Counter(get_domain(line.strip())
                       for line in f
                       if "@" in line)
print(contador)     
from bs4 import BeautifulSoup
import requests


url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html,'html5lib')


#primero = soup.find('p')
#   Esto equivale a linea de abajo
primero = soup.p

primero_text = soup.p.text.split()


# Retorna KeyError si no existe el 'ID'
p_id = soup.p['id']

# Retorna None sin o existe el 'ID'
p_id1 = soup.p.get('id')

# Retorna todo el contenido del primer '<p>'
todo_el_parrafo = soup.find_all('p')

# Retorna todos los párrafos que tenga ID
parrafo_con_ids = [p for p in soup('p') if p.get('id')]

# Retorna todos los párrafos tengan o no tengan ID
# parametro_con_ids = [p for p in soup('p')]

# Retorna párrafos de class específica
important_parrafo = soup('p', {'class': 'important'})
important_parrafo1 = soup('p', 'important')
important_parrafo2 = [p for p in soup('p')
                      if 'important' in p.get('class', [])]

span_inside_divs = [span for div in soup('div')
                    for span in div('span')]

# muestra todo el contenido de la página
print(soup.prettify())

# Muestra el texto de la página
print(soup.get_text())
print(span_inside_divs)
#print(important_parrafo)
#print(important_parrafo1)
#print(important_parrafo2)
#print(todo_el_parrafo)
#print(parrafo_con_ids)
#print(primero_text)
#print(p_id)
#print(p_id1)
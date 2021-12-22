# coding=utf-8
import os
import get_requests
import json

HEADERS = {
    'x-api-key': os.environ.get('X_API_KEY'),
    'x-request-id': "12345",
    'x-session-id': "12345",
    'authorization': "Bearer 6c18c234b1b18b1d97c7043e2e41135c293d0da9",
}
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code

print ()
#retornar todas las categorias
all_categories = get_requests.categories_all(HEADERS)
print("categories:\n",json.dumps(all_categories, indent=2))

try:
    id = int(input('¿Que categoria desea mostrar?  '))
    categorie=get_requests.categorie_by_id(id, HEADERS)
    print("categorie:\n",json.dumps(categorie,indent=2))
except ValueError:
    print("No existe esa categoria, prueba otra vez...")
except:
    print("Error no existen categorias por alfabeto.")

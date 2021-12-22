import requests
from requests.models import Response

Direcc_url = "https://api.nasa.gov/techport/api/projects/17792?api_key=avSEu7fGVWr7HBVtz2cpUDYVXxrUwT5xEMVOmz0N"


try:
    res = requests.get(Direcc_url)
    if res.status_code != 200:
        print("Verifique la direccion ".center(100, "-"))
    else:
        print("\n")
        print("Informacion de la Api consumida".center(100, '-'))
        print("\n")
        res = res.json()
        api_dict = res['project']

        for clave, valor in api_dict.items():
            nota = f'''
            clave == {clave}
            valor == {valor}
            '''
            print(nota)

except Exception as e:
        print(e)
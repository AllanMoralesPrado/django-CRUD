import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","CRUDproject.settings")
django.setup()
from CRUDapp.models import Inmuebles, Region

def get_list_inmuebles(name,descr):
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble__contains = name).filter(descripcion__contains = descr)

    archi1 = open("datos.txt","w", encoding='utf-8')
    for l in lista_inmuebles.values():
        archi1.write(str(l))
        archi1.write("\n")
    archi1.close()

    return lista_inmuebles

resultado = get_list_inmuebles("Providencia","Cocina")
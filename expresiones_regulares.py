# expresión regular 
import re
from dataclasses import dataclass


@dataclass
class Informacion:
    # datos de busqueda para partidos de futbol
    nombre = str


def busqueda(nombre):
    #Busqueda del sitio donde se jugo el partido
    pattern = re.compile(fr'^(\d\d\d\d)\-\d\d-\d\d,(.*),Friendly,{nombre}')
    return pattern


def abrir_archivo(pattern):
    # abrir archiov csv de historico de particos
    with open("C:\\Users\\dafer\\Documents\\platzi\\01_curso_expresiones_regulares\\04_archivo\\REGEX-master\\REGEX-master\\files\\results.csv","r",encoding="utf-8") as f:
        for i in iter(f.readline,""):
            resultado = re.match(pattern,i)
            if resultado:
                print(f"Juego:  {resultado.group(2)}")

    f.close()


def main():
    #Ejemplo de busqueda
    nombre = Informacion.nombre("Glasgow")
    pattern = busqueda(nombre)
    print(abrir_archivo(pattern))


if __name__=="__main__":
    main()
# expresión regular 
import re

pattern = re.compile(r'^([\d]{4,4})\-\d\d-\d\d,(.*),Friendly,.*$')

with open("C:\\Users\\dafer\\Documents\\platzi\\01_curso_expresiones_regulares\\04_archivo\\REGEX-master\\REGEX-master\\files\\results.csv","r",encoding="utf-8") as f:
    for i in iter(f.readline,""):
        resultado = re.match(pattern,i)
        if resultado:
            print(f"Juego:  {resultado.group(2)}")

    f.close()


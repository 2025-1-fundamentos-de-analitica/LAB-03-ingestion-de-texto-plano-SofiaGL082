"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd

# pylint: disable=import-outside-toplevel


def limpieza_palabra(palabra):
    return ' '.join(filter(lambda x: x!= '', palabra.split(" ")))

def limpieza(palabras):
    return ', '.join(map(limpieza_palabra, palabras.split(",")))

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    anchos = [9, 16, 16]
    titulos = [[], [], [], []]
    filas = []

    with open("files/input/clusters_report.txt") as file:
        lines = iter(file.readlines())

        # Obtener la cabecera
        for _ in range(2):
            line = next(lines).rstrip()
            i = 0
            j = 0
            for ancho in anchos:
                titulos[j].append(line[i:i+ancho].strip())
                j+=1
                i+=ancho
            titulos[j].append(line[i:].strip())
        titulos = list(map(lambda x: ' '.join(x).strip(), titulos))

        # ignorar linea vacía
        next(lines)

        # ignorar separador
        next(lines)

        # Obtener las filas
        while (line := next(lines, None)) is not None:
            i = 0
            j = 0
            fila = []
            for ancho in anchos:
                fila.append(line[i:i+ancho].strip())
                j += 1
                i+=ancho
            fila.append(line[i:].strip())

            fila[-1] = limpieza(fila[-1]).strip()

            if fila[0] == '':
                if fila[-1] == '':
                    continue
                filas[-1][-1] += " " + fila[-1]
            else:
                fila[0] = int(fila[0])
                fila[1] = int(fila[1])
                fila[2] = float(fila[2].removesuffix(" %").replace(",", "."))
                filas.append(fila)

    titulos = list(map(lambda h: h.lower().replace(" ", "_"), titulos))

    for fila in filas:
        fila[-1] = fila[-1].removesuffix(".")

    return pd.DataFrame(filas, columns=titulos)
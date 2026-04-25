import os

# Obtener la carpeta actual
carpeta_actual = os.getcwd()

# Obtener el nombre de la carpeta
nombre_carpeta = os.path.basename(carpeta_actual)

# Nombre del archivo de salida
archivo_salida = f"lista_{nombre_carpeta}.txt"

# Listar solo archivos (no carpetas)
archivos = [
    f for f in os.listdir(carpeta_actual)
    if os.path.isfile(os.path.join(carpeta_actual, f))
]

# Escribir los nombres en el archivo (uno por línea)
with open(archivo_salida, "w", encoding="utf-8") as f:
    for archivo in archivos:
        f.write(archivo + "\n")

print(f"Lista creada en: {archivo_salida}")
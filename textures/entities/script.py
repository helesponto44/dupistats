import os

carpeta = "."

prefijo = "EntitySprite_"

for nombre in os.listdir(carpeta):
    ruta_original = os.path.join(carpeta, nombre)

    # Solo archivos (no carpetas)
    if os.path.isfile(ruta_original) and nombre.startswith(prefijo):
        nuevo_nombre = nombre.replace(prefijo, "", 1)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        # Evitar sobrescribir si ya existe
        if not os.path.exists(ruta_nueva):
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado: {nombre} -> {nuevo_nombre}")
        else:
            print(f"Saltado (ya existe): {nuevo_nombre}")

print("Proceso terminado.")
def cambiar_punto_por_coma(numeros):
    numeros_formateados = [str(numero).replace('.', ',') for numero in numeros]
    return numeros_formateados

# Leer los números del archivo
numeros = []
with open('resumen.txt', 'r') as archivo:
    for linea in archivo:
        numeros.append(float(linea.strip()))  # Convertir cada línea a un número flotante y agregarlo a la lista

numeros_formateados = cambiar_punto_por_coma(numeros)

# Guardar los números formateados en otro archivo
with open('resumen_formateado.txt', 'w') as archivo:
    for numero in numeros_formateados:
        archivo.write(numero + '\n')

print("Se han guardado los números formateados en el archivo 'resumen_formateado.txt'.")

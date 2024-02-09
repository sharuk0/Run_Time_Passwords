def tiempo_para_descifrar(contra, intentos_por_segundo):
    longitud = len(contra)
    combinaciones = 94 ** longitud
    tiempo_en_segundos = combinaciones / intentos_por_segundo
    tiempo_en_horas = tiempo_en_segundos / (60 * 60)
    return tiempo_en_horas

def calcular_tiempos(input_file, output_file, intentos_por_segundo):
    with open(input_file, 'r') as file:
        contrasenhas = file.readlines()

    with open(output_file, 'w') as output:
        for contra in contrasenhas:
            tiempo = tiempo_para_descifrar(contra.strip(), intentos_por_segundo)
            tiempo_formateado = '{:,.2f}'.format(tiempo).replace('.', ',')
            output.write(f"{tiempo_formateado}\n")

# Cambia estos valores según tus necesidades
input_file = 'contrasenhas.txt'
output_file = 'tiempos_descifrado.txt'
intentos_por_segundo = 10 ** 12  # Por ejemplo, 1 billón de intentos por segundo

calcular_tiempos(input_file, output_file, intentos_por_segundo)

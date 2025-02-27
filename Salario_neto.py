# Programa para calcular el salario neto aproximado.

def devengos(base, extra, plus, horas):
    '''
    ### Utilidad:
    Calcular el total de devengos, es decir, la suma del salario base, las pagas extra y otros pagos (plus).

    ### Argumento base:
    Salario base para 40 horas semanales. Anual o mensual.
    Mensual máximo 5000€.

    *Formato* --> *float*

    ### Argumento extra:
    Sí ("S") o no ("N"). Para indicar si las pagas extra están prorrateadas o no.

    *Formato* --> *str*

    ### Argumento plus:
    Para indicar salario extra percibido, como plus de transporte u otros.

    *Formato* --> *float*

    ### Argumento horas:
    Para indicar el número de horas semanales trabajado (máximo 40h).

    *Formato* --> *float*
    '''

    base = base * horas / 40

    if base > 10000:
        # Base = anual. Si no, es que es mensual.
        base /= 12
    
    if extra == 'S':
        # Pagas extra prorrateadas.
        devengado = base + plus + (base / 6)
    else:
        # Pagas extra por separado (no se calculan).
        devengado = base + plus
    
    return float(devengado)

base = float(input('Introduce el salario base, anual o mensual, a jornada completa: '))
extra = input('Indica si tienes pagas extra prorrateadas ("S") o no ("N"): ')
plus = float(input('Si tienes otros pagos, indica la cantidad (si no, pon "0"): '))
horas = float(input('Indica las horas que trabajas a la semana (máx. 40h): '))

total_devengado = devengos(base, extra, plus, horas)

cotizaciones = float(input('Indica el porcentaje total de aportaciones de cotización: '))
irpf = float(input('Indica el porcentaje de IRPF que se te aplica: '))

total_cotizado = total_devengado * (1 - cotizaciones / 100) # El total ya con cotizaciones aplicadas.

total_liquido = total_cotizado * (1 - irpf / 100) # El total ya con cotizaciones e IRPF aplicados.

print(f'\nEl salario neto es: {round(total_liquido, 2)}€.')

total_deducido = total_liquido - total_devengado
print(f'Se te han retirado {-1 * round(total_deducido, 2)}€ en concepto de cotizaciones e IRPF.\n')

input('Pulsa cualquier tecla para salir del programa.')
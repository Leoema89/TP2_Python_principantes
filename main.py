import random
import time

RESULTADOS_APUESTA = ('Gana', 'Pierde')

def menu():
    print()
    print('>', '-' * 80, '<')
    print(' '*3, 'La ruina del apostador (Gamblers ruin)\n')
    print('1 - Simulacion unica e individual')
    print('2 - Simulacion con repeticiones consecutivas')
    print('0 - Salir')
    print('>', '-' * 80, '<')
    opcion = int(input('Ingrese la opción: '))
    return opcion


def apuestas(fichas_inicial, max_jugadas, probabilidades):
    global cant_apuestas, fichas_totales, cant_jugadas, jugada_ganada, jugada_perdida
    fichas_totales = fichas_inicial
    cant_jugadas = max_jugadas
    cant_apuestas = jugada_ganada = jugada_perdida = 0

    while fichas_totales > 0:
        jugada = random.choices(RESULTADOS_APUESTA, probabilidades, k=1)
        if jugada[0] == 'Gana':
            fichas_totales += 1
            jugada_ganada += 1
        else:
            fichas_totales -= 1
            jugada_perdida += 1
        cant_apuestas += 1
        cant_jugadas -= 1
    return cant_apuestas, fichas_totales, cant_jugadas, jugada_ganada, jugada_perdida

def sim_sucesivas():
    cant_ejecuciones = int(input('Cuantas ejecuciones desea realizar?: '))
    total_apuestas = 0
    for i in range(1,cant_ejecuciones+1,1):
        tic = time.perf_counter()
        apuestas(fichas_inicial, max_jugadas, probabilidades)  # Ejecucion de funcion
        toc = time.perf_counter()
        print('Cantidad apuestas: ', cant_apuestas)
        print('Tiempo de ejecucion de funcion', i, f': {toc-tic:0.5f} segundos')
        total_apuestas += cant_apuestas
    print('Promedio de apuestas: ', (total_apuestas/cant_ejecuciones))



fichas_inicial = int(input('Cuantas fichas tiene?: '))  # agregar validador de numero cargado
max_jugadas = int(input('Cuantas veces quiere jugar?: '))  # agrgar validador de valor cargado
prob_ganar = float(input('Probabilidad de ganar: '))  # agrgar validador de valor cargado
probabilidades = [prob_ganar, (1-prob_ganar)] #definicion de probabilidades para Weight

opcion = -1
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        apuestas(fichas_inicial,max_jugadas,probabilidades)
        if cant_apuestas >= 300: # Condicion donde llega a hacer mas de 300 apuestas
            print('Felicidades! Sobreviviste a las 300 apuestas\n', 'Cantidad de apuestas realizadas: ', cant_apuestas,
          '\nTotal de fichas: ', fichas_totales, '\nApuestas ganadas: ', jugada_ganada, '\nApuestas perdidas: ', jugada_perdida)
        else: # Condicion donde no llega a las 300 apuestas
            print('Que pena! No llegaste a las 300 apuestas\n', 'Cantidad de apuestas realizadas: ', cant_apuestas, '\nTotal de fichas: ', fichas_totales, '\nCantidad de jugadas restantes: ',cant_jugadas, '\nApuestas ganadas: ', jugada_ganada, '\nApuestas perdidas: ', jugada_perdida)

    elif opcion == 2:
        sim_sucesivas()

    elif opcion == 0:
            print("--- Programa finalizado ---")

    else:
        print("\nOpción no válida!")





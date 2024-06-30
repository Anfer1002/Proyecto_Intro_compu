import random

def mostrar(palabra, letra, adivinar):
    posicion = 0
    letras_acertadas = 0
    for x in palabra:
        if x == letra:
            adivinar[posicion] = '['+x+']'
            letras_acertadas += 1
        posicion += 1
    if posicion > 0:
        print(", ".join(map(str,adivinar)).replace(",","",-1))
    return letras_acertadas

def sacar_palabras(numero, palabras):
    if numero == 1:
        archivo = open("animales.txt", "r")   
    elif numero == 2:
        archivo = open("deportes.txt", "r")
    elif numero == 3:
        archivo = open("paises.txt", "r")
    elif numero == 4:
        archivo = open("florestplantas.txt", "r")
    elif numero == 5:
        archivo = open("todos.txt", "r")
    else:
        archivo = open("todos.txt", "r")
    linea = archivo.readline()
    archivo.close()
    acomodar = linea.split()
    for x in range(len(acomodar)):
        palabras.append(acomodar[x].upper())
    return len(acomodar)-1

def selecc_elegida(adivinar, palabras, random_num):
    for x in range(len(palabras[random_num])):
                adivinar.append([])
    return palabras[random_num]

def menu():
    adivinar = []
    palabras = []
    vidas = 10
    ganadas = 0
    perdidas = 0
    random_txt = random.randint(1, 5)
    max_lista = sacar_palabras(random_txt, palabras)
    random_num = random.randint(0, max_lista)
    elegida = selecc_elegida(adivinar, palabras, random_num)
    
    ciclo = True
    while ciclo:
        entrada = str(input('\nSeleccione una opción\n1. Jugar\n2. Cambiar parámetros\n3. Mostrar resultados\n4. Ayuda\n5. Acerca de...\n6. Salir\nOpción: '))
        
        if entrada == '1':                      
            letras_acertadas = 0
            conteo_letras = ''
            encendido = True
            while encendido:
                if vidas < 1:
                    perdidas += 1
                    print('\nTe quedaste sin vidas\nLa palabra era: ', elegida)
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
                    if seguir == '1':
                        adivinar.clear()
                        letras_acertadas = 0
                        conteo_letras = ''
                        nuevo_random = random.randint(0, max_lista)
                        elegida = selecc_elegida(adivinar, palabras, nuevo_random)                 
                    else:
                        encendido = False
                    
                elif letras_acertadas == len(elegida):
                    ganadas += 1
                    print('\nPalabra acertada')
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
                    if seguir == '1':
                        adivinar.clear()
                        nuevo_random = random.randint(0, max_lista)
                        letras_acertadas = 0
                        conteo_letras = ''
                        elegida = selecc_elegida(adivinar, palabras, nuevo_random)                 
                    else:
                        encendido = False

                else:
                    letra = str(input('\nIngrese la letra que quere comprobar o ingrese 6 para salir: ')).upper()
                    if len(letra)>1:
                        print('\nEntrada inválida.')
                    elif letra in conteo_letras:
                        print('\nEsa letra ya se ha utilizado.')
                    elif letra in (elegida) :
                        letras_acertadas += mostrar(elegida, letra, adivinar)
                        conteo_letras += letra
                    elif letra == '6':
                        encendido = False
                    else:
                        vidas -= 1
                        conteo_letras += letra
                        print('\n', letra, 'no estaba en la palabra. Ahora tienes',vidas,'vidas.')
                        
        elif entrada == '2':
            adivinar.clear()
            palabras.clear()
            opcion_1 = int(input('\nSeleccione la temática de las palabras\n1. Animales\n2. Deportes\n3. Paises\n4. Flores y plantas\n5. Todos\nOpción: '))
            if opcion_1 == 1 or 2 or 3 or 4 or 5:
                max_lista = sacar_palabras(opcion_1, palabras)
            else:
                max_lista = sacar_palabras(5, palabras)
            random_num = random.randint(0, max_lista)
            elegida = selecc_elegida(adivinar, palabras, random_num)
            
            print('\nTienes', vidas, 'vidas o intentos. Selecciona:\n1 si quieres 15 vidas\n2 si quieres 10 vidas\n3 si quieres 5 vidas\nO enter para salir.')
            opcion_2 = input('\nOpción: ')
            if opcion_2 == '1':
                vidas = 15
            elif opcion_2 == '2':
                vidas = 10
            elif opcion_2 == '3':
                vidas = 5
            else:
                print('\n:Las vidas se mantendrán en', vidas)                        
        elif entrada == '3':
            print('\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
            input('\nPresione enter para volver al menú principal. ')
            encendido = True
        elif entrada == '4':
            print('\nEstas son las instrucciones del juego.')
            input('\nPresione enter para volver al menú principal. ')  
        elif entrada == '5':
            print('\nCreado por:\nAnfernhy José Berrocal Rojas\nEsteban Josué Román Oviedo\nYurguen Chacón\nAño 2024')
            input('\nPresione enter para volver al menú principal. ')
        elif entrada == '6':
            print('\nGracias por jugar. ')
            ciclo = False 

menu()
#queda por hacer: instrucciones

#El propósito del programa es recrear un juego tipo "ahorcado" mientras ponemos en práctica los conocimientos teóricos aprendidos durante el curso.

import random

def mostrar(palabra, letra, adivinar):
    #Esta función modifica la lista "adivinar" cuando la letra dada por el usuario se encuentra dentro de la palabra por adivinar y muestra el progreso de la palabra logrado por el usuario.
    #Recibe la palabra por adivinar, la letra ingresada por el usuario y la lista con espacios que se muestra al usuario. Retorna la cantidad de veces que "letra" está contenida dentro de la palabra por adivinar.
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
    #Esta función abre el .txt correspondiente y agrega las palabras dentro de los documentos a la lista "palabras".
    #Recibe la opción(numero) para seleccionar el .txt que se debe abrir y la lista con palabras extraídas del .txt. Retorna la cantidad de palabras extraídas de los .txt.
    if numero == 1:
        archivo = open("animales.txt", "r")   
    elif numero == 2:
        archivo = open("deportes.txt", "r")
    elif numero == 3:
        archivo = open("paises.txt", "r")
    elif numero == 4:
        archivo = open("florestplantas.txt", "r")
    elif numero == 5:   
        todos_docs = ["animales.txt", "deportes.txt", "paises.txt", "florestplantas.txt"]
        for x in range(len(todos_docs)):
            archivo = open(todos_docs[x], "r")
            linea = archivo.readline()
            archivo.close()
            acomodar = linea.split()
            for x in range(len(acomodar)):
                palabras.append(acomodar[x].upper())
        return len(palabras)-1
    
    linea = archivo.readline()
    archivo.close()
    acomodar = linea.split()
    for x in range(len(acomodar)):
        palabras.append(acomodar[x].upper())
    return len(palabras)-1

def selecc_elegida(adivinar, palabras, random_num):
    #Esta función modifica la lista "adivinar" agregando espacios según la cantidad de letras que tenga la palabra por adivinar.
    #Recibe la lista con espacios que se muestra al usuario, la lista con palabras extraídas del .txt y un número aleatorio para elegir la palabra. Retorna la palabra elegida para adivinar.
    for x in range(len(palabras[random_num])):
                adivinar.append([])
    return palabras[random_num]

def menu():
    #Esta función contiene el menú y es el "cerebro" del programa. No recibe parámetros y no retorna valores.
    adivinar = []
    palabras = []
    vidas = 10
    ganadas = 0
    perdidas = 0
    random_txt = random.randint(1, 5)
    max_lista = sacar_palabras(random_txt, palabras)
    random_num = random.randint(0, max_lista)
    elegida = selecc_elegida(adivinar, palabras, random_num)

    while True:
        entrada = str(input('\nSeleccione una opción\n1. Jugar\n2. Cambiar parámetros\n3. Mostrar resultados\n4. Ayuda\n5. Acerca de...\n6. Salir\nOpción: '))
        
        if entrada == '1':                      
            letras_acertadas = 0
            conteo_letras = ''
            encendido = True
            print(", ".join(map(str,adivinar)).replace(",","",-1))
            while encendido:
                if vidas < 1:
                    perdidas += 1
                    print('\nTe quedaste sin vidas\nLa palabra era: ', elegida)
                    print('\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
                    if seguir == '1':
                        adivinar.clear()
                        letras_acertadas = 0
                        conteo_letras = ''
                        nuevo_random = random.randint(0, max_lista)
                        vidas = 10
                        print('Vidas establecidas en', vidas)
                        elegida = selecc_elegida(adivinar, palabras, nuevo_random)
                        print(", ".join(map(str,adivinar)).replace(",","",-1))
                    else:
                        encendido = False
                    
                elif letras_acertadas == len(elegida):
                    ganadas += 1
                    print('\nPalabra acertada')
                    print('\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
                    if seguir == '1':
                        adivinar.clear()
                        nuevo_random = random.randint(0, max_lista)
                        letras_acertadas = 0
                        conteo_letras = ''
                        elegida = selecc_elegida(adivinar, palabras, nuevo_random)
                        print(", ".join(map(str,adivinar)).replace(",","",-1))
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
                        print(", ".join(map(str,adivinar)).replace(",","",-1))
                        
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
            print("""\nEste es un juego tipo ahorcado. Ten en cuenta las siguientes indicaciones:
            
            - Para empezar a jugar debes seleccionar la opción 1 en el menú principal.
            - EL jugador debe digitar letras repetidamente para formar una palabra aleatoria. Las letras con tilde se consideran distintas.
            - Al inicio de la partida el usuario tiene 10 vidas o intentos.
            - En la opción 2 se pueden cambiar el número de vidas y el tema de las palabras.
            - Se mostrará en la pantalla tantos corchetes como letras hayan en la palabra por adivinar.
            - Al acertar una letra se mostrará el progreso asignando la palabra en el espacio correspondiente.
            - Si aciertas todas las letras, ganarás la partida
            - Al digitar una letra que no se encuentre en la palabra se restará una vida.  
            - Si las vidas llegan a cero, perderás la partida.
            
            ¡Buena suerte!""")
            input('\nPresione enter para volver al menú principal. ')  
        elif entrada == '5':
            print('\nCreado por:\nAnfernhy José Berrocal Rojas\nEsteban Josué Román Oviedo\nYurguen Chacón\nAño 2024')
            input('\nPresione enter para volver al menú principal. ')
        elif entrada == '6':
            print('\nGracias por jugar. ')
            ciclo = False 

menu()

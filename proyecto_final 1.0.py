#El propósito del programa es recrear un juego tipo "ahorcado" mientras ponemos en práctica los conocimientos teóricos aprendidos durante el curso.

import random   #Para generar números aleattorios
import os       #Para limpiar la interfaz
import time     #Para agregar tiempos de espera

def sacar_palabras(palabras):
    #Esta función abre todos los .txt y agrega las listas de palabras de los documentos a la lista "palabras".
    #Recibe la la lista "palabras" y no retorna valores

    todos_docs = ["animales.txt", "deportes.txt", "paises.txt", "florestplantas.txt"]
    for x in todos_docs:
        archivo = open(x, "r")
        linea = archivo.readline().upper()
        archivo.close()
        palabras.append(linea.split())

def selecc_elegida(adivinar, palabras, tema):
    #Esta función modifica la lista "adivinar" agregando espacios según la cantidad de letras que tenga la palabra por adivinar.
    #Recibe la lista con espacios que se muestra al usuario, la lista con palabras extraídas del .txt y un número para elegir el tema.
    #Retorna la palabra elegida para adivinar.
    
    if 0<=tema<=3:
        pos_palabra = random.randint(0, len(palabras[tema])-1)
        for x in range(len(palabras[tema][pos_palabra])):
                adivinar.append([])
        return palabras[tema][pos_palabra]
    
    else:
        tema_random = random.randint(0,3)
        pos_palabra = random.randint(0, len(palabras[tema_random])-1)
        for x in range(len(palabras[tema_random][pos_palabra])):
                adivinar.append([])    
        return palabras[tema_random][pos_palabra]

def modificar_adivinar(palabra, letra, adivinar):
    #Esta función modifica la lista "adivinar" cuando la letra dada por el usuario se encuentra dentro de la palabra por adivinar.
    #Recibe la palabra por adivinar, la letra ingresada por el usuario y la lista con espacios que se muestra al usuario.
    #Retorna la cantidad de veces que "letra" está contenida dentro de la palabra por adivinar.

    posicion = 0
    letras_acertadas = 0
    for x in palabra:
        if x == letra:
            adivinar[posicion] = '['+x+']'
            letras_acertadas += 1
        posicion += 1
    return letras_acertadas

def menu():
    #Esta función contiene el menú y es el "cerebro" del programa. No recibe parámetros y no retorna valores.
    adivinar = []
    palabras = []
    vidas = 10
    ganadas = 0
    perdidas = 0
    sacar_palabras(palabras)
    tema = random.randint(0,4)
    elegida = selecc_elegida(adivinar, palabras, tema)
    
    ciclo = True
    while ciclo:
        entrada = input('\nSeleccione una opción\n1. Jugar\n2. Cambiar parámetros\n3. Mostrar resultados\n4. Ayuda\n5. Acerca de...\n6. Salir\nOpción: ')
        
        if entrada == '1':                      
            letras_acertadas = 0
            conteo_letras = ''
            
            encendido = True
            while encendido:
                print(", ".join(map(str,adivinar)).replace(",","",-1))
                
                if vidas < 1:
                    perdidas += 1
                    print('\nTe quedaste sin vidas\nLa palabra era: ', elegida, '\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
                
                    if seguir == '1':
                        adivinar.clear()
                        letras_acertadas = 0
                        conteo_letras = ''
                        vidas = 10
                        print('Vidas establecidas en', vidas)
                        elegida = selecc_elegida(adivinar, palabras, tema)
                    
                    else:
                        encendido = False
                        os.system('cls')
                    
                elif letras_acertadas == len(elegida):
                    ganadas += 1
                    print('\n¡Palabra acertada!\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
                    seguir = input('\nSi deseas sequir jugando presiona 1 o enter para salir\nOpción: ')
    
                    if seguir == '1':
                        adivinar.clear()
                        letras_acertadas = 0
                        conteo_letras = ''
                        vidas = 10
                        print('Vidas establecidas en', vidas)
                        elegida = selecc_elegida(adivinar, palabras, tema)
                        
                    else:
                        encendido = False
                        os.system('cls')

                else:
                    letra = str(input('\nIngrese la letra que quere comprobar o ingrese 6 para salir: ')).upper()
                    os.system('cls')
                
                    if len(letra)>1:
                        print('\nEntrada inválida.')
                    
                    elif letra in conteo_letras:
                        print('\nEsa letra ya se ha utilizado.')
                    
                    elif letra in elegida:
                        letras_acertadas += modificar_adivinar(elegida, letra, adivinar)
                        conteo_letras += letra
                    
                    elif letra == '6':
                        encendido = False
                        os.system('cls')

                    else:
                        vidas -= 1
                        conteo_letras += letra
                        print(letra, 'no estaba en la palabra. Ahora tienes', vidas,'vidas.')
                              
        elif entrada == '2':
            adivinar.clear()
            opcion_1 = int(input('\nSeleccione la temática de las palabras\n1. Animales\n2. Deportes\n3. Paises\n4. Flores y plantas\n5. Todos\nOpción: '))-1
            if opcion_1 == 0 or 1 or 2 or 3 or 4:
                elegida = selecc_elegida(adivinar, palabras, opcion_1)
            else:
                elegida = selecc_elegida(adivinar, palabras, opcion_1=4)
            
            print('\nTienes', vidas, 'vidas o intentos por defecto.\nSi deseas cambiar esta cantidad de vidas, puedes elegir cualquier número entre 5 y 15.')
            opcion_2 = int(input('\nOpción: '))
            if 5<=opcion_2<=15:
                vidas = opcion_2
                print('Ahora tienes', vidas, 'vidas.')
            else:
                print('\nLas vidas se mantendrán en', vidas)
            
            time.sleep(3)
            os.system('cls')
                 
        elif entrada == '3':
            print('\nHas ganado', ganadas, 'partidas.\nHas perdido', perdidas, 'partidas.')
            input('\nPresione enter para volver al menú principal. ')
            os.system('cls')

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
            os.system('cls')

        elif entrada == '5':
            print('\nCreado por:\nAnfernhy José Berrocal Rojas\nEsteban Josué Román Oviedo\nYurguen Steve Chacón Solórzano\nAño 2024')
            input('\nPresione enter para volver al menú principal. ')
            os.system('cls')

        elif entrada == '6':
            print('\nGracias por jugar. ')
            ciclo = False 

#Este es el programa principal
menu()
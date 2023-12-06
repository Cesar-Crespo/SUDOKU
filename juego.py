import os
import random

cantidad_filas = 0 #cantidad de filas del tablero de sudoku
cantidad_columnas = 0 #cantidad de columnas del tablero de sudoku
opcion_insertar = 1 # opcion 1 insertar numero en el tablero sudoku
opcion_resolver_sudoku = 2
opcion_salir = 3 # opcion 3 salir del menu
minimo_valor = 1 # numero minimo que se puede insertar en el tablero sudoku
maximo_valor = 0 # numero maximo que se puede insertar en el tablero sudoku


'''	
meetodo que explica las reglas del juego dependiendo del nivel
'''
def reglas_sudoku ():
	if nivel == 1 :
		print ("usted eligio el nivel facil")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 4")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante 2x2")
	elif nivel == 2 :
		print ("usted eligio el nivel medio ")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 6")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante 2x3")	
	elif nivel == 3:
		print ("usted eligio el nivel dificil ")
		print ("las reglas de este juego consisten en: ")
		print ("insertar un numero entre el 1 y el 9")
		print ("el numero ingresado no se debe repetir ni en fila ni en columnas ni en el cuadrante 3x3")


''''
creamos una matriz para ambos niveles
'''

facil_1 = [
    [1, 0, 3, 0],
	[0, 0, 0, 0],
	[3, 0, 1, 0],
	[0, 1, 0, 3]
]

facil_2 = [
    [3, 0, 4, 0],
	[0, 0, 0, 0],
	[1, 0, 3, 0],
	[0, 3, 0, 4]
]

facil_3 = [
    [2, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 4, 0],
    [0, 2, 0, 1]
]

medio_1 = [
    [1, 0, 0, 0, 4, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 5, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 3, 0],
    [0, 3, 0, 0, 0, 0]
]

medio_2 = [
    [3, 0, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 4, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 5, 0],
    [0, 1, 0, 0, 0, 0]
]

medio_3 = [
    [6, 0, 0, 0, 1, 0],
    [0, 0, 0, 4, 0, 0],
    [0, 1, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 6, 0],
    [0, 2, 0, 0, 0, 0]
]


dificil_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

dificil_2 = [
    [5, 1, 0, 0, 8, 0, 0, 0, 0],
    [8, 0, 0, 5, 4, 9, 0, 0, 0],
    [0, 4, 9, 0, 0, 0, 0, 8, 0],
    [1, 0, 0, 0, 7, 0, 0, 0, 2],
    [4, 0, 0, 9, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 1, 0, 0, 0, 9],
    [0, 7, 0, 0, 0, 0, 6, 4, 0],
    [0, 0, 0, 7, 9, 5, 0, 0, 7],
    [0, 0, 0, 0, 7, 0, 0, 2, 5]
]


dificil_3 = [
    [8, 5, 0, 0, 2, 0, 0, 0, 0],
    [6, 0, 0, 8, 3, 4, 0, 0, 0],
    [0, 4, 3, 0, 0, 0, 0, 6, 0],
    [3, 0, 0, 0, 4, 0, 0, 0, 2],
    [5, 0, 0, 3, 0, 7, 0, 0, 4],
    [9, 0, 0, 0, 6, 0, 0, 0, 5],
    [0, 9, 0, 0, 0, 0, 1, 4, 0],
    [0, 0, 0, 4, 7, 8, 0, 0, 6],
    [0, 0, 0, 0, 9, 0, 0, 5, 8]
    ]


'''
metodo que verifica si el valor ya se encuentra en la fila indicada del tablero, en caso de existir retorna true, caso contrario retorna false
'''
def validar_fila(f, valor, tablero):
	for c in range(cantidad_columnas):
		if tablero[f][c] == valor:
			return False
	return True 

'''
metodo que verifica si el valor ya se encuentra en la columna indicada del tablero, en caso de existir retorna true, caso contrario retorna false
'''
def validar_columna(c, valor, tablero):
	for f in range(cantidad_filas):
		if tablero[f][c] == valor:
			return False
	return True
'''
metodo que verifica si el valor ya se encuentra en el cuadrante indicado por su fila (f) y columna(c) del tablero , en caso de existir retorna true, caso contrario retorna false
'''
def validar_cuadrante_2x2(f, c, valor, tablero):
    inicio_fila = (f//2)*2
    inicio_columna = (c//2)*2
    for i in range(inicio_fila, inicio_fila + 2):
        for j in range(inicio_columna, inicio_columna + 2):
            if tablero[i][j] == valor:
                return False
    return True

def validar_cuadrante_2x3(f, c, valor, tablero):
    inicio_fila = (f // 2) * 2
    inicio_columna = (c // 3) * 3
    for i in range(inicio_fila, inicio_fila + 2):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == valor:
                return False
    return True

def validar_cuadrante_3x3(f, c, valor, tablero):
    inicio_fila = (f // 3) * 3
    inicio_columna = (c // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == valor:
                return False
    return True
'''
metodo que verifica si el valor se encuentra del rango permitido de numeros que acpeta el tablero sudoku, estar, en caso de estar demtro del rango retorna true, caso contrario retorna false
'''
def validar_valor(valor):
	return valor >= minimo_valor and valor <= maximo_valor
'''
metodo que verifica que se cumplam todas las condiciones para insertar un valor en el tablero sudoku en la fila (f) y columna(c) indicada, en caso de cumplirla retorna true, caso contrario retorna false
'''
def validar(f, c, valor, tablero):
    if nivel == 1:
        return (validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_2x2(f, c, valor, tablero))
    elif nivel == 2:
        return (validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_2x2(f, c, valor, tablero))
    elif nivel == 3:
        return (validar_valor(valor)
                and validar_fila(f, valor, tablero)
                and validar_columna(c, valor, tablero)
                and validar_cuadrante_2x2(f, c, valor, tablero))

	            
'''
metodo que no permite modificar esas posiciones si la fila o columna indican una posicion en la cual ya esta determinado un numero no se podra insertar sobre el , si no se cumple las condiciones entonces se podra insertar el numero
'''
def insertar_valor(f, c, valor, tablero):
    if nivel == 1 and ((f == 0 and c == 0) or (f == 0 and c == 2) or (f == 2 and c == 0) or (f == 2 and c == 2) or (f == 3 and c == 1) or (f == 3 and c == 3)):
        print("Esa posicion es fija y no se puede modificar")
    elif nivel == 2 and ((f == 0 and c == 0) or (f == 0 and c == 4) or (f == 1 and c == 3) or (f == 2 and c == 1) or (f == 2 and c == 5) or (f == 4 and c == 3) or (f == 4 and c == 4) or ( f == 5 and c == 1)):
        print("Esa posicion es fija y no se puede modificar")
    elif nivel == 3 and ((f == 0 and c == 0) or (f == 0 and c == 1) or (f == 0 and c == 4) or (f == 1 and c == 0) or (f == 1 and c == 3) or (f == 1 and c == 4) or (f == 1 and c == 5) or (f == 2 and c == 1) or (f == 2 and c == 2) or (f == 2 and c == 7) or (f == 3 and c == 0) or (f == 3 and c == 4) or (f == 3 and c == 8) or (f == 4 and c == 0) or (f == 4 and c == 3) or (f == 4 and c == 5) or (f == 4 and c == 8) or (f == 5 and c == 0) or (f == 5 and c == 4) or (f == 5 and c == 8) or (f == 6 and c == 1) or (f == 6 and c == 6) or (f == 6 and c == 7) or (f == 7 and c == 3) or (f == 7 and c == 4) or (f == 7 and c == 5) or (f == 7 and c == 8) or (f == 8 and c == 4) or (f == 8 and c == 7) or (f == 8 and c == 8)):
        print("Esa posicion es fija y no se puede modificar")
    else:
        tablero[f][c] = valor
    return tablero
'''
metodo que imprime el tablero de sudoku
'''
def mostrar_tablero(tablero):
	for m in tablero:
		print(m)
'''
metodo que imprime el nivel del juego
'''
def selccion_niveles ():
	print ("seleccione el nivel en el que desea jugar")
	print ("1) Nivel facil ")
	print ("2) Nivel medio")
	print ("3) Nivel dificil")
	
'''
metodo que te muestra el sudoku ya resuelto dependiendo del nivel 
'''
def sudoku_resuelto ():
	if nivel == 1:
		if genera_tab_facil == 1:
			tab_resuelto = [
				[1, 2, 3, 4],
				[4, 3, 2, 1],
				[3, 4, 1, 2],
				[2, 1, 4, 3]
            ]
			for m in tab_resuelto:
				print (m)
		elif genera_tab_facil == 2:
			tab_resuelto = [
				[3, 2, 4, 1],
				[4, 1, 2, 3],
				[1, 4, 3, 2],
				[2, 3, 1, 4]
            ]	
			for m in tab_resuelto:
				print(m)
		else:
			tab_resuelto = [
				[2, 4, 1, 3],
                [3, 1, 2, 4],
                [1, 3, 4, 2],
                [4, 2, 3, 1]
            ] 	
			for m in tab_resuelto:
				print (m)
	elif nivel ==2:
		if genera_tab_medio == 1:
			tab_resuelto = 	[
				[1, 3, 5, 6, 4, 2],
                [6, 4, 2, 5, 1, 3],
                [3, 5, 1, 4, 2, 6],
                [2, 6, 4, 3, 5, 1],     
                [4, 1, 6, 2, 3, 5],
                [5, 3, 2, 1, 6, 4]
			]
			for m in tab_resuelto:
				print (m)
		if genera_tab_medio == 2:
			tab_resuelto = [
				[3, 5, 1, 6, 2, 4],
                [2, 6, 4, 1, 3, 5],
                [5, 4, 2, 3, 1, 6],
                [1, 3, 6, 5, 4, 2],
                [6, 2, 3, 4, 5, 1],
                [4, 1, 5, 2, 6, 3]
			]
			for m in tab_resuelto:
				print(m)
		else:
			tab_resuelto = [
			   [6, 3, 4, 5, 1, 2],
			   [1, 5, 2, 4, 3, 6],
			   [2, 1, 3, 6, 4, 5],
			   [4, 6, 5, 3, 2, 1],
			   [5, 4, 1, 2, 6, 3],
			   [3, 2, 6, 1, 5, 4]
			]
			for m in tab_resuelto:
				print(m)
	else:
		if genera_tab_dificil == 1:
			tab_resuelto = [
				[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
				]
			for m in tab_resuelto:
				print(m)
		elif genera_tab_dificil ==2:	
			tab_resuelto = [
				[5, 1, 7, 2, 8, 6, 4, 9, 3],
                [8, 3, 2, 5, 4, 9, 7, 1, 6],
                [6, 4, 9, 1, 3, 7, 2, 8, 5],
                [1, 5, 3, 8, 7, 4, 9, 6, 2],
                [4, 6, 8, 9, 2, 3, 5, 7, 1],
                [7, 2, 5, 6, 1, 8, 3, 4, 9],
                [9, 7, 1, 3, 5, 2, 6, 4, 8],
                [2, 8, 4, 7, 9, 5, 1, 3, 7],
                [3, 9, 6, 4, 7, 1, 8, 2, 5]
			]
			for m in tab_resuelto:
				print(m)	
		else:
			tab_resuelto = [
				[8, 5, 7, 1, 2, 6, 4, 3, 9],
                [6, 1, 9, 8, 3, 4, 5, 2, 7],
                [2, 4, 3, 7, 5, 9, 8, 6, 1],
                [3, 7, 1, 9, 4, 5, 6, 8, 2],
                [5, 2, 6, 3, 8, 7, 9, 1, 4],
                [9, 8, 4, 2, 6, 1, 3, 7, 5],
                [7, 9, 8, 5, 1, 2, 1, 4, 3],
                [1, 3, 5, 4, 7, 8, 2, 9, 6],
                [4, 6, 2, 6, 9, 3, 7, 5, 8]
			]
			for m in tab_resuelto:
				print(m)
'''
metodo que imprime el menu del juego 
'''	
def menu( ):
	print("-------------------😎Menu😎------------------")
	print("Debe seleccionar una opcion escribiendo el numero")
	print("1) Insertar valor")
	print("2) ver sudoku resuelto")
	print("3) Salir")
'''
metodo que ingresa un mensaje al ganador 
'''

if __name__== "__main__":
	resp = 0
	nivel = 0
	
	while nivel == 0 or nivel > 3:
		selccion_niveles ()
		nivel = int (input("escriba el numero de la opcion : "))

	if nivel == 1:
		genera_tab_facil = random.randint(1,3)
		if genera_tab_facil == 1:
			facil = facil_1
		elif genera_tab_facil ==2:
			facil = facil_2
		else :
			facil = facil_3
			
		tablero = facil
		cantidad_columnas = 4
		cantidad_filas = 4
		maximo_valor = 4		
	elif nivel == 2:
		genera_tab_medio = random.randint(1,3)
		if genera_tab_medio ==1:
			medio = medio_1
		elif genera_tab_medio == 2:
			medio = medio_2
		else:
			medio = medio_3
		tablero = medio	
		cantidad_columnas = 6
		cantidad_filas = 6
		maximo_valor = 6
	elif nivel == 3 :
		genera_tab_dificil = random.randint(1,3)
		if genera_tab_dificil ==1:
			dificil = dificil_1
		elif genera_tab_dificil == 2:
			dificil = dificil_2
		elif genera_tab_dificil == 3:
			dificil = dificil_3
		tablero = dificil	
		cantidad_columnas = 9
		cantidad_filas = 9
		maximo_valor = 9
		
	def nivel_superado(tablero):
		for fila in tablero:
			for valor in fila:
				if valor == 0:
					return False
		return True
	

	while (resp != opcion_salir ):
		if nivel_superado(tablero):
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Nivel Superado, ¡¡Has completado el SUDOKU!!")
			break
		os.system('cls' if os.name == 'nt' else 'clear')
		print("                  ✨ SUDOKU ✨              ")
		reglas_sudoku()
		mostrar_tablero(tablero)
		menu( )	
		resp = (input("Escriba el numero de la opcion :"))
		if resp.isdigit():
			resp = int(resp)
			if resp == opcion_salir:
				break
			elif resp == opcion_resolver_sudoku:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("                  ✨ Sudoku Resuelto ✨              ")
				sudoku_resuelto()
				break
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("                  ✨ SUDOKU ✨              ")
				reglas_sudoku()
				mostrar_tablero(tablero)
				menu()
				v = input("Introduzca el valor a introducir en el tablero:")
				if v.isdigit():
					v = int(v)
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				f = input("Introduzca la fila del tablero: ")
				if f.isdigit():
					f = int(f) - 1
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				c = input("Introduzca la columna del tablero: ")
				if c.isdigit():
					c = int(c) - 1
				else:
					print("Por favor, ingrese solo números.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
				es_valido = validar(f, c, v, tablero)
				if es_valido:
					tablero = insertar_valor(f, c, v, tablero)
				else:
					print("Error al introducir el número, intente nuevamente.")
					continue  # Vuelve a hacer la pregunta si la entrada es invalida
					

		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Error")
			input("Presione Enter para continuar")
	else:
		print ("error")
		input ("presione enter para cotinuar")
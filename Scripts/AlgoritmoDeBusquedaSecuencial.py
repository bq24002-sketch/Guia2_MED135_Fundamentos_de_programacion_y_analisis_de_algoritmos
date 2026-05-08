#Algoritmo de Busqueda Secuencial
numeros = [4, 8, 15, 23, 42]
objetivo = 23
encontrado = False
for i in range( len(numeros) ):
	      if numeros [ i ] == objetivo:
               print( "Elemento encontrado en la posición:", i )
               encontrado = True
               break
if not encontrado:
         print( "Elemento no encontrado" )

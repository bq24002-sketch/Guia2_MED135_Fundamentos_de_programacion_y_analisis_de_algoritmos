#Algoritmo de Busqueda Binaria

numeros = [3, 7, 12, 18, 25, 31, 40]
objetivo = 25
inicio = 0
fin = len(numeros) - 1
while inicio <= fin:
     medio = (inicio + fin) // 2

     if numeros[medio] == objetivo:
         print("Elemento encontrado en la posición:", medio)
         break

     elif numeros[medio] < objetivo:
        inicio = medio + 1
     else:
        fin = medio - 1

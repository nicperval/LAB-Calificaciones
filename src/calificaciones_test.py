from calificaciones import *
if __name__ == '__main__':
#Ejercicio 1
#A
    print(nota_teoria(9.1,7.2))
    print(nota_teoria(4,6))
    print(nota_teoria(4,3))
    print(nota_teoria(None,3))
    print(nota_teoria(9,None))
#B
    print(nota_cuatrimestre((9.1,7.2),8.1))
    print(nota_cuatrimestre((4,6),5))
    print(nota_cuatrimestre((4,3),None))
    print(nota_cuatrimestre((None,3),None))
    print(nota_cuatrimestre((9,None),4.5))
#C
    print (nota_continua((9.6, 9.9,10.0, 9.8),(9.7,9.5)))
    print (nota_continua((4.4, 4.9, 5.1, 4.7),(4.6,4.8)))
    print (nota_continua((4.0, 6.0, 4.0, 3.0),(5.0, None)))
    print (nota_continua((9.0, None, 4.0, 3.0),(4.5, None)))
    

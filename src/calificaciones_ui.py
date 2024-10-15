from calificaciones import *
def solicita_notas():
    nombre = input("Introduzca su nombre: ")

    teoria = lee_notas("teoria", 5)
    practica = lee_notas("practica", 3)
    return (nombre,teoria,practica)

def lee_notas(tipo_examen,numero_notas):
    res = []
    for i in range(1,numero_notas):
        mensaje = f"Introduzca la nota del examen de {tipo_examen} {i} (- si no se ha presentado):"
        nota = input(mensaje)
        nota = a_real(nota)
        nota = a_cero(nota)
        res.append(nota)
    return res

def a_real(nota):
    if nota == '-':
        res = None
    else:
        res = float(nota)
    return res

def mostrar_notas(datos):
    print(f"Hola, {datos[0]}")
    t1 = (datos[1][0],datos[1][1])
    t2 = (datos[1][2],datos[1][3])
    teoria_c1 = nota_teoria(datos[1][0],datos[1][1])
    teoria_c2 = nota_teoria(datos[1][2],datos[1][3])
    cuatrimestre1 = nota_cuatrimestre(t1,datos[2][0])
    cuatrimestre2 = nota_cuatrimestre(t2,datos[2][1])
    continua = nota_continua(datos[1],datos[2])
    print("Tus notas del primer cuatrimestre son:")
    print(f"teoria {teoria_c1},practica {datos[2][0]}, cuatrimestre {cuatrimestre1}")
    print("Tus notas del segundo cuatrimestre son:")
    print(f"teoria {teoria_c2},practica {datos[2][1]}, cuatrimestre {cuatrimestre2}")
    print(f"Tu nota final de la asignatura es {continua}")
if __name__ == '__main__':
    mostrar_notas(solicita_notas())
    
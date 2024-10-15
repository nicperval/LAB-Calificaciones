#Ejercicio 1
#A
def nota_teoria(nt1,nt2):
    t1 = a_cero(nt1)
    t2 = a_cero(nt2)
    media=(t1+t2)/2
    return media
def a_cero(nota):
    res = nota
    if nota is None:
        res = 0
    return res
#B
def nota_cuatrimestre(t,np):
    media_t = nota_teoria(t[0],t[1])
    if media_t >= 4:
        t1 = a_cero(t[0])
        t2 = a_cero(t[1])
        p = a_cero(np)
        res = 0.1 * (t1+t2) + 0.8 * p
    else:
        res = 0
    return res
#C
def nota_continua(teorico,practico):
    t1 = a_cero(teorico[0])
    t2 = a_cero(teorico[1])
    t3 = a_cero(teorico[2])
    t4 = a_cero(teorico[3])
    tc1 = (t1,t2)
    tc2 = (t3,t4)
    p1 = a_cero(practico[0])
    p2 = a_cero(practico[1])
    nc1 = nota_cuatrimestre(tc1,p1)
    nc2 = nota_cuatrimestre(tc2,p2)
    if nc1 >= 4:
        if nc2 >= 4:
            res = (nc1+nc2)/2
        else:
            nc2 = 0.1 * (t3+t4) + 0.8 * p2
            res = min(nc1,nc2)
    else:
        nc1 = 0.1 * (t1+t2) + 0.8 * p1
        nc2 = 0.1 * (t3+t4) + 0.8 * p2
        res = min(nc1,nc2,4)
    return res

if __name__ == '__main__':
    print (nota_continua((4.0, 6.0, 4.0, 3.0),(5.0, None)))
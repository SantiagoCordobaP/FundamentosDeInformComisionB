#Practica N°1
#ejercicio1
s= input("Ingresar Texto Largo:")
print (len(s))

#ejercicio2
s1= input("Ingresar Texto 5ta y 6ta:")
print(s1[5] + s1[6])

#ejercicio3
s3= input ("Como es tu nombre y apellido?:")
print ("hola, " +  s3)

#ejercicio4
s41 = input ("como es tu nombre?:")
s42 = input ("como es tu 1er apellido?:")
s43 = input ("como es tu 2do apellido?:")

#ejercicio5
s5 = input ("3 numeros:")
suma = (int(s5[0]) + int(s5[2]) + int(s5[4]))/3
print(suma)

#ejercicio6
s6= input("minutos:")
horas= (int(s6)//60)
minutos = int(s6) - (int(horas)* 60)
print(("horas:") + str(horas) + " y minutos: " + str(minutos))

#ejercicio7
s71= input ("sueldo base: ")
s72= input ("venta: ")
Fin_de_mes = int(s71) + (int(s72)* 0.10)

#ejercicio8
s8= [input("respuesta 1: "), input("respuesta 2: "), input("respuesta 3: ")]
nota = 0
for respuesta in s8:
    if respuesta == "correcta":
        nota+= 4
    elif respuesta == "incorrecta":
        nota+=1
    else:
        nota
print(nota)
alumnos=int(input("Introduzca el número de alumnos: "))
for j in range(alumnos):
    tnota=0
    notas=int(input(f"Introduzca el número de notas del alumno {j+1}: "))
    for i in range(notas):
        nota=float(input(f"Nota {i+1}: "))
        tnota=tnota+nota

    resultado=tnota/notas

    if resultado>=4:
        print("El promedio es",round(resultado, 1)","," alumno aprobado")
    else:
        print("El promedio es",round(resultado, 1)","," alumno reprobado")






# num=int(input("Introduzca un número: "))
# total=0

# for i in range(num):
#     total=total+i+1

# print("La sumatoria es", total)

# vocales=0
# conso=0
# nigga=input("Introduzca su nombre: ")

# for i in nigga:
#     print(i)
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#     elif i==" ":
#         conso+0
#     else:
#         conso=conso+1
# print(f"El total de vocales es", vocales)
# print(f"El total de consonantes es", conso)


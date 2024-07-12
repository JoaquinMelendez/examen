import random
import csv
import os

bajo800 = []
bajo2 = []
mayor2 = []

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]
def mCSV():
    with open("BBDD/BaseSueldos.csv", "w", newline='', encoding = "utf-8") as Doc:
        csv.writer(Doc)

def asignar_sueldos():

    filas = []
    
    for trabajador in trabajadores:
        
        sueldo = random.randrange(300000, 2500000)

        fila = [trabajador, sueldo]
        filas.append(fila)
        
    with open("BBDD/BaseSueldos.csv", "a", newline='', encoding = "utf-8") as Doc:
        escribir = csv.writer(Doc)
        escribir.writerows(filas)
    
    print("Se han insertado correctamente los sueldos")
    input("Pulse ENTER para continuar")

def clasificar_sueldos():

    menos800k = []
    bt800ky2m = []
    mas2m = []
    
    with open("BBDD/BaseSueldos.csv", "r", newline='') as Doc:
        read = csv.reader(Doc)
        
        for fila in read:
            nombre, sueldo = fila[0], int(fila[1])
            if sueldo < 800000:
                menos800k.append((nombre, sueldo))
            elif 800000 <= sueldo <= 2000000:
                bt800ky2m.append((nombre, sueldo))
            elif sueldo > 2000000:
                mas2m.append((nombre,sueldo))

    totalSueldos = 0

    for nombre, sueldo in menos800k:
        totalSueldos += sueldo
    for nombre, sueldo in bt800ky2m:
        totalSueldos += sueldo
    for nombre, sueldo in mas2m:
        totalSueldos += sueldo

    print("---SUELDOS MENORES A $800.000---")
    print(f'TOTAL: {len(menos800k)}\n')
    print("Nombre empleado\t Sueldo")
    for nombre, sueldo in menos800k:
        print(f'{nombre}\t ${sueldo}')
    print("")

    print("---Entre $800.000 y $2.000.000---")
    print(f'TOTAL: {len(bt800ky2m)}\n')
    print("Nombre empleado\t Sueldo")
    for nombre, sueldo in bt800ky2m:
        print(f'{nombre}\t ${sueldo}')
    print("")


    print("---Más de $2.000.000---")
    print(f'TOTAL: {len(mas2m)}\n')
    print("Nombre empleado\t Sueldo")
    for nombre, sueldo in mas2m:
        print(f'{nombre}\t ${sueldo}')
    print("")

    print(f'\n\t TOTAL SUELDOS: ${totalSueldos}')

    print("")
    input("Pulse ENTER para volver al menú")

def ver_estadisticas():

    sueldos = []

    with open("BBDD/BaseSueldos.csv", "r", newline='') as Doc:
        read = csv.reader(Doc)
        
        for fila in read:
            sueldo = int(fila[1])
            sueldos.append(sueldo)
    
    sueldoMasAlto = 0
    sueldoMasBajo = 3000000

    promedioSueldos = (sum(sueldos)/len(sueldos))
    promedioSueldos = round(promedioSueldos, 0)
    

    for sueldo in sueldos:
        
        if sueldo > sueldoMasAlto:
            sueldoMasAlto = sueldo
        if sueldo < sueldoMasBajo:
            sueldoMasBajo = sueldo

    print("--- RESUMEN ESTADISTICAS ---\n")
    print(f'Sueldo más alto: ${sueldoMasAlto}')
    print(f'Sueldo más bajo: ${sueldoMasBajo}')
    print(f'Promedio de sueldos: ${promedioSueldos}')
    print(f'Media geométrico: ?')

    print("")
    input("Pulse ENTER para continuar")

def reporte_sueldos():

    with open("BBDD/ReporteSueldos.csv", "w", newline='') as Doc:
        write = csv.writer(Doc)
        write.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo líquido"])
            
        with open("BBDD/BaseSueldos.csv", "r", newline='') as Doc:
            read = csv.reader(Doc)

            for fila in read:
                nombre, sueldo = fila[0], int(fila[1])

                dctoSalud = sueldo * 0.07
                dctoSalud = int(round(dctoSalud, 0))
                dctoAFP = sueldo * 0.12
                dctoAFP = int(round(dctoAFP, 0))
                sueldoLiquido = sueldo - dctoSalud - dctoAFP
                
                nombreEmpleado = nombre
                sueldoBase = "$" + str(sueldo)
                dcto_Salud = "$" + str(dctoSalud)
                dcto_AFP = "$" + str(dctoAFP)
                sueldo_liquido = "$" + str(sueldoLiquido)

                write.writerow([nombreEmpleado, sueldoBase, dcto_Salud, dcto_AFP, sueldo_liquido])

    
    with open("BBDD/ReporteSueldos.csv", "r", newline='') as Doc:
        read = csv.reader(Doc)
        next(read)

        print(f"{'Nombre empleado':<20}{'Sueldo Base':<15}{'Descuento Salud':<20}{'Descuento AFP':<20}{'Sueldo Líquido':<20}")
        for fila in read:
            nombre, sueldo, descuento_salud, descuento_afp, sueldo_liquido = fila
            print(f"{nombre:<20}{sueldo:<15}{descuento_salud:<20}{descuento_afp:<20}{sueldo_liquido:<20}")
        print("Pulse Enter para volver al menú")
        input("")

mCSV()

while True:

    os.system("clear")

    print("""--- Aplicación de Reportes de sueldos ---

    Seleccione una opción:
    1- Asignar sueldos
    2- Clasificar sueldos
    3- Estadísticas
    4- Reporte de sueldos
    5- Salir""")

    opc = input("Digite su opción: ")

    if opc not in ["1", "2", "3", "4", "5"]:
        print("Seleccione una opción válida")
        input("Pulse ENTER para continuar")

    os.system("clear")

    if opc == "1":
        asignar_sueldos()
    if opc == "2":
        clasificar_sueldos()
    if opc == "3":
        ver_estadisticas()
    if opc == "4":
        reporte_sueldos()
    if opc == "5":
        os.system("clear")
        break

print("Finalizando programa... Desarrollado por Joaquín Meléndez. Rut: 20.535.543-k")
    



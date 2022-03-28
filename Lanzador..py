'''
Proyecto 33: Beisbol (Lanzadores)
En el béisbol, un lanzador, es el jugador que lanza la pelota desde el montículo hacia el receptor, con el objetivo
de sacar al bateador e impedirle anotar carreras. Para evaluar la efectividad de los lanzadores se toma en cuenta
la cantidad de carreras permitidas y el número de entradas lanzadas. Para cada lanzador de la liga se debe
suministrar:
Nombre del lanzador, cantidad de carreras permitidas, y entradas lanzadas
Desarrolle un programa que determine e imprima:
Para cada lanzador:
1. Efectividad del lanzador.
2. Estatus del lanzador.
Para todos los lanzadores:
3. Nombre del lanzador con menor efectividad, si hay otros lanzadores con la misma efectividad aparte de él contarlos.
4. % de lanzadores cuya efectividad está entre 2.51 y 3
Consideraciones
Para calcular la efectividad usamos: 𝐸𝑓𝑒𝑐𝑡𝑖𝑣𝑖𝑑𝑎𝑑=𝐶𝑎𝑟𝑟𝑒𝑟𝑎_𝑃𝑒𝑟𝑚𝑖𝑡𝑖𝑑𝑎𝑠∗9/𝐸𝑛𝑡𝑟a𝑑𝑎𝑠_𝐿𝑎𝑛𝑧𝑎𝑑𝑎𝑠
Para el estatus aplicamos la siguiente tabla:
Efectividad      Estatus
Menor de 2.00 - Excelente
Entre 2.00 y 2.50 - Muy buena
Entre 2.51 y 3.00 - Buena
Entre 3.01 y 3.50 - Regular
Mayor a 3.50 - Mala
'''
# Apertura de archivos.
arch1 = open("lanzadores.txt", "r")
arch2 = open("estatus.txt", "w")
# Inicialización de variables.
nombre_lanz_menor_ef = ""
band = 0
cont_menor_ef = 0
cont_ef_menor = 0
cont_lanzadores = 0
cont_lanz_buena = 0

for contenido in arch1:
    linea = contenido.split(",")
    # Datos de entrada.
    nombre = str(linea[0])
    cant_carreras = int(linea[1])
    num_ent = int(linea[2])
    # Pregunta 4
    cont_lanzadores += 1
    # Pregunta 1 y 2.
    efectividad = (cant_carreras * 9)/num_ent
    if efectividad < 2:
        arch2.write(nombre + " tiene estatus excelente."+ "\n")
    elif efectividad >= 2 and efectividad <= 2.50:
        arch2.write(nombre + " tiene estatus muy bueno." + "\n")
    elif efectividad >= 2.51 and efectividad <= 3.00:
        arch2.write(nombre + " tiene estatus bueno." + "\n")
        # Pregunta 4.
        cont_lanz_buena += 1
    elif efectividad >= 3.01 and efectividad <= 3.50:
        arch2.write(nombre + " tiene estatus regular." + "\n")
    else:
        arch2.write(nombre + " tiene estatus malo." + "\n")
    # Pregunta 1.    
    print(nombre, "tiene una efectividad de", efectividad)
    # Pregunta 3.
    if band == 0:
        nombre_lanz_menor_ef = nombre
        menor_ef = efectividad
        cont_menor_ef = 0
        band = 1
    elif efectividad < menor_ef:
        nombre_lanz_menor_ef = nombre
        menor_ef = efectividad
        cont_menor_ef = 0
    elif efectividad == menor_ef:
        cont_menor_ef += 1
# Salida de datos.
# Pregunta 3.
if band == 1:
    print(nombre_lanz_menor_ef, "es el lanzador con menor efectividad y", cont_menor_ef, "lanzadores aparte de él tienen esa misma efectividad.")
# Pregunta 4.
if cont_lanzadores !=0:
    porc = (cont_lanz_buena/cont_lanzadores) * 100
    print("El porcentaje de lanzadores cuya efectividad está entre 2.51 y 3 es", porc, "%")
else:
    print("No hubo lanzadores jugando.")
# Cierre de archivos.
arch1.close()
arch2.close()
        
        
        
        



































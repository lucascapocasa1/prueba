# MENU ##
#LUCASLUCASLUCASLUCASCLUCASCLUASC#

opcion = input("Pulse 1 para elegir duracion, 2 para configurar probabilidades, 3 para iniciar partida, 4 para ver el ranking, o 5 para salir.")

flag_salir = False

while not flag_salir:
    #while opcion != 5:

    if opcion == "1":

        pass

        opcion = input("Pulse 1 para elegir duracion, 2 para configurar probabilidades, 3 para iniciar partida, 4 para ver el ranking, o 5 para salir.")


    elif opcion == "2":

        pass

        opcion = input("Pulse 1 para elegir duracion, 2 para configurar probabilidades, 3 para iniciar partida, 4 para ver el ranking, o 5 para salir.")

    elif opcion == "3":

        pass
           
        opcion = input("Pulse 1 para elegir duracion, 2 para configurar probabilidades, 3 para iniciar partida, 4 para ver el ranking, o 5 para salir.")

    elif opcion == "4":

        pass

        opcion = input("Pulse 1 para elegir duracion, 2 para configurar probabilidades, 3 para iniciar partida, 4 para ver el ranking, o 5 para salir.")

    else opcion == "5":

        flag_salir = True 







# VALIDACION ##


if(opcion == 1):
        pregunta_modificacion(cursos)
    elif(opcion == 2):
        listar_cursos(cursos) #Que cuesten mas de 1150$
    elif(opcion == 3):
        cargar_asistentes(cursos)
    elif(opcion == 4):
        mostrar_cursos(cursos)

"""Daniel Robles Meza | ING EN DESARROLLO DE SOFTWARE"""

import os
import time

users = {}
NewPassword = " "
luces = 0
ventiladores = 0
enchufes = 0
newRoom=(" ")
newLock=(" ")


os.system (' CLS ')

Welcome = "Smart Home"

print (Welcome.center (150 ," "))

def showInfo (info):

     if info==(" "):
         print ("\nNo hay nada registrado")
         time.sleep(1.6)

     else:
         print("Estas son las que se encuentran registaradas:")
         print(info)

def showInfo(info):
    if info == "":
        print("\nNo hay nada registrado")
        time.sleep(1.6)
    else:
        print("Estas son las que se encuentran registaradas:")
        print(info)


def RegisterDevice():
    global luces, ventiladores, enchufes

    print(" ")
    print("Tipos de Dispositivos: ")
    print("\n 1-Luces \n 2-Ventiladores \n 3-Enchufes\n")

    tipoDispositivo = int(input("Ingrese el tipo de Dispositivo que desea agregar: "))

    if tipoDispositivo == 1:
        nombre = input("Ingrese el nombre de las luces: ")
        estado = input("Ingrese el estado inicial de las luces (Encendido/Apagado): ").lower()
        if estado == "encendido":
            print(f"Luces '{nombre}' agregadas y están encendidas.")
        elif estado == "apagado":
            print(f"Luces '{nombre}' agregadas y están apagadas.")
        else:
            print("Estado ingresado no válido.")
            time.sleep(1.6)

        #programación automática
        opcion_programacion = input("¿Desea configurar la programación automática para este dispositivo? (s/n): ").lower()
        if opcion_programacion == "s":
            dia = input("Ingrese el día en que desea que las luces se enciendan (Lunes, Martes, etc.): ")
            hora = input("Ingrese la hora en que desea que las luces se enciendan (24 horas): ")

            componentes_hora = hora.split(':')
            if len(componentes_hora) == 2:
                try:
                    hora = int(componentes_hora[0])
                    minuto = int(componentes_hora[1])
                    if 0 <= hora < 24 and 0 <= minuto < 60:
                        print(f"Luces '{nombre}' programadas para encenderse el {dia} a las {hora}.")
                    else:
                        print("Hora ingresada no válida.")
                except ValueError:
                    print("Formato de hora incorrecto.")
            else:
                print("Formato de hora incorrecto.")
                time.sleep(1.6)

    elif tipoDispositivo == 2:
        nombre = input("Ingrese el nombre del ventilador: ")
        estado = input("Ingrese el estado inicial del ventilador (Encendido/Apagado): ").lower()
        if estado == "encendido":
            print(f"Ventilador '{nombre}' agregado y está encendido.")
        elif estado == "apagado":
            print(f"Ventilador '{nombre}' agregado y está apagado.")
        else:
            print("Estado ingresado no válido.")
            time.sleep(1.6)

        # programación automática
        opcion_programacion = input("¿Desea configurar la programación automática para este dispositivo? (s/n): ").lower()
        if opcion_programacion == "s":
            dia = input("Ingrese el día en que desea que el ventilador se encienda (Lunes, Martes, etc.): ")
            hora = input("Ingrese la hora en que desea que el ventilador se encienda (24 horas): ")

            componentes_hora = hora.split(':')
            if len(componentes_hora) == 2:
                try:
                    hora = int(componentes_hora[0])
                    minuto = int(componentes_hora[1])
                    if 0 <= hora < 24 and 0 <= minuto < 60:
                        print(f"Ventilador '{nombre}' programado para encenderse el {dia} a las {hora}.")
                    else:
                        print("Hora ingresada no válida.")
                except ValueError:
                    print("Formato de hora incorrecto.")
            else:
                print("Formato de hora incorrecto.")
                time.sleep(1.6)

    elif tipoDispositivo == 3:
        nombre = input("Ingrese el nombre del enchufe: ")
        estado = input("Ingrese el estado inicial del enchufe (Encendido/Apagado): ").lower()
        if estado == "encendido":
            print(f"Enchufe '{nombre}' agregado y está encendido.")
        elif estado == "apagado":
            print(f"Enchufe '{nombre}' agregado y está apagado.")
        else:
            print("Estado ingresado no válido.")
            time.sleep(1.6)

        #programación automática
        opcion_programacion = input("¿Desea configurar la programación automática para este dispositivo? (s/n): ").lower()
        if opcion_programacion == "s":
            dia = input("Ingrese el día en que desea que el enchufe se encienda (Lunes, Martes, etc.): ")
            hora = input("Ingrese la hora en que desea que el enchufe se encienda (24 horas): ")

            componentes_hora = hora.split(':')
            if len(componentes_hora) == 2:
                try:
                    hora = int(componentes_hora[0])
                    minuto = int(componentes_hora[1])
                    if 0 <= hora < 24 and 0 <= minuto < 60:
                        print(f"Enchufe '{nombre}' programado para encenderse el {dia} a las {hora}.")
                    else:
                        print("Hora ingresada no válida.")
                except ValueError:
                    print("Formato de hora incorrecto.")
            else:
                print("Formato de hora incorrecto.")
                time.sleep(1.6)

    else:
        print("\nTipo de dispositivo no válido")
        time.sleep(1.6)

def viewDevice():
    global luces, ventiladores, enchufes
    
    if ventiladores > 0:
        print("Ventiladores registrados: ", ventiladores)
        time.sleep(1.6)
    elif luces > 0:
        print("Luces registradas: ", luces)
        time.sleep(1.6)
    elif enchufes > 0:
        print("Enchufes registrados: ", enchufes)
        time.sleep(1.6)
       
       

# Menu Principal
while True:
    os.system (' CLS ')
    
    print (Welcome.center (150 ," "))
    
    print (" ")
    
    print ("1- Ingresar")
    
    print (" ")
    
    print ("2- Registrarse")
    
    print (" ")
    
    print ("3- Ver Usuarios Existentes ")
    
    print (" ")
    
    print ("4- Salir ")
    
    print (" ")
    
    rp = int(input("Ingrese la opción que desee: "))
    
    # Apartado Ingresar Usuario
    if rp == 1:
        os.system (' CLS ')
        
        print (Welcome.center (150 ," "))
        
        print (" ")
       
        user = input("Ingrese su usuario: ")
        
        if user in users:
            correct_password = users[user]
            FrequentPassWord = (input("Ingrese su contraseña o su pin: "))
            if FrequentPassWord == correct_password:
                os.system (' CLS ')
        
                print (Welcome.center (150 ," "))
                
                print("Bienvenido,", user)
                
                time.sleep(1.6)
                 
                print (" ")
                backmenu = 0
                while True:
                    
                    #Apartado para agregar una habitacion

                    os.system (' CLS ')
        
                    print (Welcome.center (150 ," "))

                    if backmenu == 1:
                        break
                
                    
                    
                    print ("¿Qué desea hacer?\n")
                    option=input("1-Registrar una habitacion \n\n2-Ver habitaciones registradas\n\n3-Registrar cerraduras \n\n4-Registrar Dispositivo\n\n5-Ver Dispositivo\n\n6- Actualizar Pin\n\n7-Cerrar sesion\n\nIngrese la opción que desee: ")

                    time.sleep(1.6)
                    
                    if option==("1"):
                        newRoom=input("\nIngrese el nombre de la habitacion: ")
                        print ("\nSe ha registrado la habitacion: ",newRoom)
                        input ("Enter para ir al menu principal")
                        
                        time.sleep(1.6)

                        
                    elif option==("2"):

                        showInfo(newRoom)
                        input ("Enter para ir al menu principal")

                        time.sleep(1.6)

                    #Registrar una cerradura

                        
                    elif option==("3"):
                        while True:
                            os.system (' CLS ')
                            print ("\n\n¿Qué desea hacer?\n")
                            option=input("1-Registrar una cerradura \n\n2-Ver cerraduras registradas \n\n3-Cambiar estado de la cerradura \n\n4-Menu anterior\n\nIngrese la opción que desee: ")
                            
                            
                            if option==("1"):
                                while True:
                                    newLock=input("\nIngrese el nombre de la cerradura: ")
                                    status=input("\nIngrese el estado de la cerradura: \n\n1-Abierta\n2-Cerrada")
                                    
                                    if status =="1":
                                        status="Abierta"
                                        break
                                    elif status =="2":
                                        status="Cerrada"
                                        break
                                    else:
                                        print ("Esa opcion no es valida")

                                    while True:
                            
                                        lock=input("Ingrese el codigo de apertura de 4 digitos")
                                        if len(lock) < 4:
                                            print ("\n Pin muy corto,", len(lock)," digitos de 4") 
                                            time.sleep(1.6)
                                        else:
                                            print("Pin regsitrado \n")
                                            input ("Enter para ir al menu principal")
                                            time.sleep(1.6)
                                            break
                                    
                            elif option==("2"):

                                 showInfo(newLock)
                                 if newLock!=(" "):
                                     print ("El estado de la cerradura es:",status)
                                     
                                 input ("Enter para ir al menu principal")

                                 time.sleep(1.6)

                            elif option==("3"):

                                 showInfo(newLock)
                                 print ("**El estado de la cerradura es:",status,"**")
                                 actualLock=input("Ingrese el pin para cambiar la cerradura")
                                 
                                 if actualLock==lock:
                                     status=input("\nIngrese el nuevo estado de la cerradura: \n\n1-Abierta\n2-Cerrada")
                                     if status =="1":
                                        status="Abierta"
                                        break
                                     elif status =="2":
                                        status="Cerrada"
                                        break
                                     else:
                                        print ("Esa opcion no es valida")
                                        
                                     input ("Enter para ir al menu principal")
                                     time.sleep(1.6)
                                 else:
                                     print("Pin incorrecto")
                                     input ("Enter para ir al menu principal")
                                     time.sleep(1.6)
                                 
                            elif option==("7"):
                                 print("Saliendo")
                        
                                 time.sleep(1.6)
                                 break

                            else:
                                print("Esa opcion no es valida")   
                    
                
                    elif option == ("4"):
                        RegisterDevice ()
                        
                    elif option == ("5"):
                        viewDevice ()
                        
                    elif option == ("6"):
                        
                        currentpin = input ("Ingrese su pin actual: \n")
                        if currentpin == newPin:
        
                            currentpin = newPin
        
                            while True:
                                newPin = input("Ingrese su nuevo pin: ")
            
                                if len(newPin) < 4:
                                    print ("\n Pin muy corto,", len(newPin)," digitos de 4") 
                                    time.sleep(1.6)
                                else:
                                    print("Pin regsitrado \n")
                                    time.sleep(1.6) 
                                    backmenu = backmenu + 1
                                    break
                        else:
                            print ("Contraseña equivocada ")
                            time.sleep(1.6)
                        
                    elif option==("7"):
                        print("Saliendo")
                        
                        time.sleep(1.6)
                        break
                    else:
                        print("Esa opcion no es valida")
            else:
                print("Contraseña invalida, Intentelo de nuevo")
                
                time.sleep(1.6)  
                
        else:
            print ("Usuario Incorrecto, intentelo de nuevo")
           
            time.sleep(1.6)  
       
    # Apartado Registrar Usuario
    if rp == 2:
        
        os.system('cls')
        print(Welcome.center(150, " "))
        print("\nCreación de Usuario, contraseña ó pin:")
        print("\n** IMPORTANTE SU CONTRASEÑÁ DEBE DE INCLUIR LO SIGUIENTE: **")
        print("\n -Una letra en Mayuscula\n", "-Número\n", "-Minimo 8 Caracteres")
        print("\n** IMPORTANTE SU PIN DEBE DE INCLUIR LO SIGUIENTE: **")
        print("\n-4 Digitos minimo")

        new_user = input("\nCree su Usuario: ")
        if new_user in users:
            print("\nEl usuario ya existe. Por favor, elija otro nombre de usuario.")
            input("\nPresione ENTER para continuar...")
            continue

        password_choice = int(input("\n[1] Para crear PIN  [2] Para crear Contraseña: "))
        if password_choice == 1:
            while True:
                new_pin = input("\nCree un PIN: ")
                if len(new_pin) < 4:
                    print("\nPin muy corto. Debe tener al menos 4 dígitos.")
                    time.sleep(1.6)
                else:
                    print("\nPIN registrado.")
                    users[new_user] = new_pin
                    time.sleep(1.6)
                    break
        elif password_choice == 2:
            while True:
                new_password = input("\nCree su Contraseña: ")
                if any(char.isupper() for char in new_password) and any(char.isdigit() for char in new_password) and len(new_password) >= 8:
                    print("\nContraseña registrada.")
                    users[new_user] = new_password
                    time.sleep(1.6)
                    break
                else:
                    print("\nError, la contraseña debe incluir al menos una mayúscula, un número y tener una longitud mínima de 8 caracteres.")
                    time.sleep(1.6)
        else:
            print("\nOpción no válida.")
            time.sleep(1.6)

        email = input("\nIngrese su Correo Electronico: ")
        input("\nSe ha registrado el usuario con éxito. Presione ENTER para volver al menú principal...")
    elif rp == 3:
        os.system('cls')
        print(Welcome.center(150, " "))
        print("\nCantidad de Usuarios: ")
        print("\nUsuarios Registrados:")
        if not users:
            print("\nNo hay usuarios registrados")
        else:
            for user in users:
                print(user)
        input("\nPresione ENTER para volver al menú principal...")
    elif rp == 4:
        print("\nVuelve pronto :)")
        time.sleep(1.6)
        break
    else:
        print("\nOpción no válida. Por favor, ingrese una opción válida.")
        time.sleep(1.6)
            
       
    
    # Ver usuarios existentes       
    if rp == 3:
        os.system('cls')
        print(Welcome.center(150, " "))
        print("\nCantidad de Usuarios: ")
        print("\nUsuarios Registrados:")
        if not users:
            print("\nNo hay usuarios registrados")
        else:
            for user in users:
                print(user)
        input("\nPresione ENTER para volver al menú principal...")
    elif rp == 4:
        print("\nVuelve pronto :)")
        time.sleep(1.6)
        break
    else:
        print("\nOpción no válida. Por favor, ingrese una opción válida.")
        time.sleep(1.6)
        
        
    # Salir del programa
    if rp == 4:
        os.system (' CLS ')
        
        print (Welcome.center (150 ," "))
        
        print (" ")
        
        print ("Vuelve pronto :)")
        
        time.sleep(1)
        
        break
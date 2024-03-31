"""Daniel Robles Meza | ING EN DESARROLLO DE SOFTWARE"""

import os
import time

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
       
        FrequentUSer = input("Ingrese su usuario: ")
        
        if FrequentUSer == NewUSer:
            FrequentPassWord = (input("Ingrese su contraseña o su pin: "))
            if FrequentPassWord == NewPassword or FrequentPassWord == newPin:
                os.system (' CLS ')
        
                print (Welcome.center (150 ," "))
                
                print("Bienvenido,", FrequentUSer)
                
                time.sleep(1.6)
                 
                print (" ")
                while True:
                    
                    #Apartado para agregar una habitacion
                    
                    os.system (' CLS ')
        
                    print (Welcome.center (150 ," "))

                
                    print ("¿Qué desea hacer?\n")
                    option=input("1-Registrar una habitacion \n\n2-Ver habitaciones registradas\n\n3-Registrar cerraduras \n\n4-Cerrar sesion\n\nIngrese la opción que desee: ")

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
                                while true:
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
                                 
                            elif option==("4"):
                                 print("Saliendo")
                        
                                 time.sleep(1.6)
                                 break

                            else:
                                print("Esa opcion no es valida")                                
                
                
                        
                    elif option==("4"):
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
        os.system (' CLS ')
        
        print (Welcome.center (150 ," "))
        
        print (" ")
        
        print ("Creación de Usuario, contraseña y pin:")
        
        print (" ")
        
        print ("** IMPORTANTE SU CONTRASEÑÁ DEBE DE INCLUIR LO SIGUIENTE: **")
        
        print (" ")
        
        print (" -Una letra en Mayuscula\n","-Número\n","-Minimo 8 Caracteres")
        
        print (" ")
        
        NewUSer = input("Cree su Usuario: ")
        
        print (" ")
        
        while True:
            NewPassword = input("Cree su Contraseña: ")
            
            print (" ")
            
            Mayuscula = False
            Num = False
                
            for mayus in NewPassword:
                if mayus.isupper () == True:
                     Mayuscula = True
            if not Mayuscula:
                print ("Error, debe de incluir al menos una mayuscula")
                time.sleep(1.6)
            
            for carac in NewPassword:
                if carac.isdigit ()  == True:
                    Num = True 
            if not Num:
                print ("La contraseña tiene que tener al menos un numero")
                time.sleep(1.6)
                
            if len(NewPassword) < 8:
                print ("Contraseña muy corta", len(NewPassword),"de 8") 
                time.sleep(1.6)  
            else:
                print("Contraseña regsitrada\n")
                time.sleep(1.6)
                break

        while True:
                
            newPin = input("Cree un de PIN de 4 digitos: ")
            
            if len(newPin) < 4:
                print ("\n Pin muy corto,", len(newPin)," digitos de 4") 
                time.sleep(1.6)
            else:
                print("Pin regsitrado \n")
                time.sleep(1.6)
                break
            
        email=input("Ingrese su Correo Electronico: ")
        input("\nSe ha registrado el usuarion con exito, ENTER para volver al menu principal")
            
       
    
    # Ver usuarios existentes       
    if rp == 3:
        os.system (' CLS ')
        
        print (Welcome.center (150 ," "))
    
        print (" ")
        
        print ("Cantidad de Usuarios: ")
    
        print (" ")
        
        if not NewUSer:
            print ("No hay usuarios registrados")
        else:
            print (NewUSer)
            
            print (" ")
        
            input ("Enter para ir al menu principal")
        
        
    # Salir del programa
    if rp == 4:
        os.system (' CLS ')
        
        print (Welcome.center (150 ," "))
        
        print (" ")
        
        print ("Vuelve pronto :)")
        
        time.sleep(1)
        
        break

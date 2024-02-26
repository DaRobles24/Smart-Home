"""Daniel Robles Meza | ING EN DESARROLLO DE SOFTWARE"""

import os
import time

os.system (' CLS ')

Welcome = "Smart Home"

print (Welcome.center (150 ," "))

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
            FrequentPassWord = (input("Ingrese su contraseña: "))
            if FrequentPassWord == NewPassword:
                os.system (' CLS ')
        
                print (Welcome.center (150 ," "))
                
                print("Bienvenido,", FrequentUSer)
                
                time.sleep(1.6)
                 
                print (" ")
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
        
        print ("Creación de Usuario y contraseña:")
        
        print (" ")
        
        print ("** IMPORTANTE SU CONTRASEÑÁ DEBE DE INCLUIR LO SIGUIENTE: **")
        
        print (" ")
        
        print (" -Una letra en Mayuscula\n","-Número\n","-Minimo 8 Caracteres")
        
        print (" ")
        
        NewUSer = input("Cree su Usuario: ")
        
        print (" ")
        
        NewPassword = input("Cree su Contraseña ")
        
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
            input("Creación Exitosa ENTER para volver al Menú")
       
    
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
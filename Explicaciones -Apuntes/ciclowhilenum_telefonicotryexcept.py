fono=''

#-- len es para limitar el numero de letras de un string-Pero como fono es un numero se convierte en string con 
#--str(fono)   
#--En este caso se usa una condicion que se niega para probar excepciones en caso de que el codigo se rompa ante cualquier error de entrada


while len(str(fono))!=9: #--desde el principio se entra en el ciclo.
    #--El ciclo asume desde el principio no se ha ingresado la condicion de 9 digitos que permite que el ciclo se rompa.
    fono=input('introduce numero de 9 digitos')
    #--si la entrada tiene menos de 9 digitos entra aca
    if len(fono)!=9:
        print('no tiene 9 digitos')
    else: #Else ayuda a que se ejecute otro codigo con la excepcion.Ya que no se cumplio la condicion se intenta un try para volver a intentar una entrada
        try:#--En caso de que si se cumpla digitos de 9.
            fono=int(fono) #--Convierte el str en int para que no haya incompatibilidad de tipos entre str e int
        except:#--En caso que se cumplan 9 digitos pero no sean digitos si no otros caracteres
            print('solo numeros')
        fono=''  #--Es para poder pedir la entrada otra vez en caso que se introduzca entrada que no sean numeros
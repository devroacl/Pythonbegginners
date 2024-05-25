
fono=''

while len(fono)!=9 or not fono.isdigit():
    fono=input('ingrese un numero de 9 digitos')
    if len(fono)==9 and fono.isdigit():
        print('tu numero es valido')
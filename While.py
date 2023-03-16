respuesta='N'
num_preguntas=0
while respuesta =='N':
    print('Hola, que tal')
    respuesta=input ('Quiere salir de la ejecucion del programa?[S/N] ')
    num_preguntas+=1
    if num_preguntas:
        print('Alcanzo el numero maximo de preguntas')
        break
else:
    print('Usted, decidio salir')

print("Adios...")

respuesta='N'
num_res_vali=0
while respuesta=='N':
    print('Hola, Que tal')
    respuesta=input('Quiere salir de la ejecucion del programa? [S/N]')
    if respuesta not in 'SN':
        respuesta='N'
        continue
    num_res_vali+=1
print('el numero de respuesta validad', num_res_vali)
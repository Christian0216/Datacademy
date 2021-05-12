def run():
    print('''
        BIENVENIDO(A) AL CONVERSOR DE MILLAS A KILOMETROS Y VICEVERSA.
        
        POR FAVOR SELECCIONA ALGUNA DE LAS DOS OPCIONES DE CONVERSIÓN:
        
        1 - MILLAS A KILOMETROS
        2 - KILOMETROS A MILLAS
        ''')
    sel = int(input('¿Y tu seleccion es?: '))
    if sel == 1:
        ml = float(input('¿Cuantas Millas deseas convertir?: '))
        print(str(ml), 'Millas son', str(ml*1.609344), 'Kilometros')
    elif sel == 2:
        km = float(input('¿Cuantos Kilometros deseas convertir?: '))
        print(str(km), 'Kilometros son', str(km/1.609344), 'Millas')
    else:
        print('Por favor Selecciona opciones 1 o 2')
    print('¡Que tengas un Excelente Dia!')    



if __name__ == '__main__':
    run()
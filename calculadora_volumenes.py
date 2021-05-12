def run():
    print('''
        BIENVENIDO(A) A LA CALCULADORA DE VOLUMENES.
        
        POR FAVOR SELECCIONA ALGUNA DE LAS SIGUIENTES OPCIONES:
        
        1 - CALCULO DE CILINDRO
        2 - CALCULO DE CUBO
        3 - CALCULO DE PARALELOGRAMO
        4 - CALCULO DE PRISMA TRIANGULAR
        ''')
    sel = int(input('¿Y tu seleccion es?: '))
    if sel == 1:
        rad = float(input('Ingresa radianes:'))
        h = float(input('Ingresa la altura:'))
        print('¡¡¡ EL VOLÚMEN DE TU CILINDRO ES', str(3.14*rad**2*h), 'M3 !!!')
    elif sel == 2:
        s = float(input('Ingresa la longitud de sus lados: '))
        print('¡¡¡ EL VOLÚMEN DE TU CUBO ES', str(s**3), 'M3 !!!')
    elif sel == 3:
        s1 = float(input('Ingresa la longitud de una de sus bases: '))
        s2 = float(input('Ingresa la longitud de la otra base: '))
        h = float(input('Ingresa la longitud de sus altura: '))
        print('¡¡¡ EL VOLÚMEN DE TU PARALELOGRAMO ES', str(s1*s2*h), 'M3 !!!')
    elif sel == 4:
        print('Para este calculo primero pedimos la base y altura del triangulo, luego la altura del prisma')
        tb = float(input('Ingresa la base del triangulo: '))
        th = float(input('Ingresa la altura del triangulo: '))
        p = float(input('Ingresa la altura del prisma: '))
        print('¡¡¡ EL VOLÚMEN DE TU PRISMA ES', str(((tb*th)/2)*p), 'M3 !!!')

if __name__ == '__main__':
    run()
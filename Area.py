def run():
    print(''' 
        
        BIENVENIDO AL CALCULADOR DE TRIANGULOS
        
        ''')
    
    s1 = int(input('Agrega el primer lado del triangulo por favor: '))
    s2 = int(input('Agrega el segundo lado del triangulo por favor: '))
    s3 = int(input('Agrega el tercer lado del triangulo por favor: '))
    if s1 == s2 and s1 == s3:
        r = 'Equilatero'
    elif s1 == s2 or s1 == s3 or s2 == s3:
        r = 'Isoceles'
    else:
        r = 'Escaleno'

    base = float(input('Agrega la base del triangulo por favor: '))
    high = float(input('Agrega la altura del triangulo por favor: '))
    area = (base * high) / 2
    
    print('Calculando.')
    print('Calculando..')
    print('Calculando...')
    print('Segun mis calculos')
    print('Tu triangulo es:', r)
    print('Y su Área es de:', str(area))


if __name__ == '__main__':
    run()
import os

def run():
    n1 = int(input('Ingresa un Numero: '))
    os.system('clear')
    n2 = int(input('Ingresa otro Numero (mayor): '))
    os.system('clear')
    n3 = int(input('Ingresa de nuevo otro numero (cualquiera): '))
    while True:
        if n3 < n2 and n3 > n1:
            break
        elif n3 > n2 or n3 < n1:
            print('Tu numero es:', str(n3))
            n3 = int(input('Intenta de nuevo con otro numero: '))
    print('Excelente, tu numero de la suerte es:', str(n3))

if __name__ == '__main__':
    run()
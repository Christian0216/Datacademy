import os

def ppt():
    player1 = 0
    player2 = 0
    while True :
        if player1 == 2 or player2 ==2:
            break
        j1 = input('Jugador 1, ¿Piedra, Papel o Tijera?:' ).capitalize()
        os.system('clear')
        j2 = input('Jugador 2, ¿Piedra, Papel o Tijera?:' ).capitalize()
        os.system('clear')
        if j1 == 'Piedra' and j2 == 'Papel' or j1 == 'Tijera' and j2 == 'Piedra' or j1 == 'Papel' and j2 == 'Tijera':
            player2 +=1
            w = 'Jugador 2'
        else:
            player1 +=1
            w = 'Jugador 1'
        print('Jugador 1 sacó:', j1)
        print('Jugador 2 sacó:', j2)
        print('Esta ronda la gana: ', w)
        print('Jugador 1:', str(player1), '-', 'Jugador 2:', str(player2))
        input('Presiona Enter para seguir')
        os.system('clear')
    if player1 == 2:
        g = 'Jugador 1'
    else:
        g = 'Jugador 2'
    return g


def run():
    print('¡¡¡GANADOR', ppt()+'!!!')


if __name__ == '__main__':
    run()
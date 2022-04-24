import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un nÃºmero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un nÃºmero mÃ¡s grande')
        else:
            print('Busca un nÃºmero mÃ¡s pequeÃ±o')
        numero_elegido = int(input('Elige otro nÃºmero: '))
    print('Â¡Ganaste!')


if __name__ == '__main__':
    run()
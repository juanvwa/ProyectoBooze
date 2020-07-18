import random

def status():
    nombre = input('Ingrese el nombre suyo :')
    dic = {'1' : 'Camarada Vodka',
           '2' : 'Sargento cerveza',
           '3' : 'Capitan Aguardiente',
           '4' : 'Mayor vino',
           '5' : 'Coronel Ron',
           '6' : 'Compadre Tequila',
           '7' : 'General Whiskey' }
    estatus = dic.get(f'{random.randint(1, 7)}')

    print(f'Saludos {nombre} su estatus es {estatus}' )

if __name__ == "__main__":
    status()

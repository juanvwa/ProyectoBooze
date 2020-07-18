import random
dic = {'1' : 'Camarada Vodka' , '2' : 'Sargento cerveza' , '3' : 'Capitan Aguardiente' , '4' : 'Mayor vino' , '5' : 'Coronel Ron' , '6' : 'Compadre Tequila' , '7' : 'General Whiskey' }

contador = random.randint(1, 7)

estatus = dic.get(f'{contador}')

nombre = input('Ingrese el nombre suyo :')

print(f'Saludos {nombre} su estatus es {estatus}' )


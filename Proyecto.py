import random
dic = {'1' : 'Camarada Vodka' , '2' : 'Sargento cerveza' , '3' : 'Capitan Aguardiente' , '4' : 'Mayor vino' , '5' : 'Coronel Ron' , '6' : 'Almirante Tequila' , '7' : 'General Whiskey' }

contador = random.randint(0, 8)

estatus = dic.get(f'{contador}')

nombre = input('Ingrese el nombre suyo :')

print(f'Saludos {nombre} su estatus es {estatus}' )


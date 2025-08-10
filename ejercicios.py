#data = input('Ingresa un dato: ')

#lista = ['hello', 'world', 'praise', 'the', 'sun']

#if lista.count(data) > 0:
#    print('El dato existe')

#else:
#    print('el dato: ', dato, 'no existe:(')
    
valor1 = input('ingrese el primer numero: ')

try:
    valor1 = int(valor1)
except:
    valor1 = 'praise the sun'

if valor1 == 'praise the sun':
    print('El valor no es un entero.')
    exit()

valor2 = input('ingrese el segundo numero: ')

try:
    valor2 = int(valor2)
except:
    valor2 = 'praise the sun'

if valor2 == 'praise the sun':
    print('El valor no es un entero.')
    exit()

operacion = input('Ingresa operacio: ')

if operacion == '+':
    print(valor1 + valor2)
elif operacion == '-':
    print(valor1 - valor2)
elif operacion == '*':
    print(valor1 * valor2)
elif operacion == '/':
    print(f"{valor1 / valor2:.2f}")
else:
    print('La operacion no es valida')


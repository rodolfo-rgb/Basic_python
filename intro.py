# Este es una pruba de algunas cosas basicas de python como: comentarios, variables y concatenaciones.

if 3 > 5:
    print('Esto no se va a imprimir')

if 5 > 3: 
    print('Praise the sun')


# variables
x = 5
y = 'praise the sun'

#print(x, y)

correo = 'rodo.aparicio.lopez@gmail.com'

#print(correo)

_my_var = 'Solaire'
MIVAR = 'Artorias'
a, b, c = 'Lordran', 'London', 'Lothric'

#print(a, b, c)

val1 = val2 = val3 = 'Gwing lord of cinder'

#print(val1, val2, val3)



# concatenacion
begin = ' Praise'
end = ' the sun'

#print(begin + end)


# Tipos de datos

string = 'Hello world'

int = 34
float = 2.5
complex = 1j

#print(int, float, complex)

# listas

lista = [1, 2, 3, 3]

# Metodos para listas
lista2 = lista.copy()
lista.append(4)
#list.clear()

#print(len(lista), lista2.count(3))

#print(lista[1])


#print(lista)
#list.pop() # remover el ultimo dato de una lista
#list.remove(2) # remover el dato por su valor
lista.reverse()
#print(lista)
lista.sort() #para ordenar una lista deben tener todas el mismo tipo de dato
#print(lista)

tupla = ('hello', 'world', 'praise', 'the')

#print(tupla.index('world'))
#print(tupla[1])
listTuple = list(tupla)

listTuple.append('sun')
#print(listTuple)

# ranges

rango = range(5)
#print(rango)

# diccionarios

dictionary = {
    'name': 'Bailey',
    'race': 'Goden',
    'age': 7
    
}

#print(dictionary)
#print(dictionary['age'])
#print(dictionary.get('age'))

dictionary['name'] = 'Krypto'
#print(dictionary)

dictionary['bark'] = 'YES'

#print(dictionary)
#dictionary.pop('bark')
#dictionary.popitem()
copy1 = dictionary.copy()
del copy1['bark']
#print(copy1)

copy2 = dict(dictionary)
dictionary.clear()
#print(dictionary, copy2)

gardfield = {
            'name': 'Gardfield',
            'age': 7
        }

bailey = {
            'name': 'Bailey',
            'age': 7
        }

gatos = {
        'Gardfield': gardfield,
        'Bailey': bailey
        }

print(gatos)

perritos = dict(name='Krypto', age=6)
print(perritos)

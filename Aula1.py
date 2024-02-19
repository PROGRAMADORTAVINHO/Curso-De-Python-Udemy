"""
DocString

"""

print(12, 34, sep= "-") # Sep : Separado
print(56, 78, sep= '/')

# Escape -> \
print("João \"Otavio\"")

# A função type mostra o tipo que o Python inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1))
print(type(10 == 10))
print(type(False))
print(type(1.1), type(-1), type(0.0))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)
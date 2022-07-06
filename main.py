nome_pessoa = 'Pessoa' #String
idade_pessoa = 10 #Int
peso_pessoa = 78.5 #Float
altura_pessoa = 1.69 #Float



nome_pessoa1 = input("Qual o seu nome: ")
idade_pessoa1 = input("Qual a sua idade: ")
peso_pessoa1 = input("Qual o seu peso: ")
altura_pessoa1 = input("Qual a sua altura: ")

nome_pessoa2 = input("Qual o seu nome: ")
idade_pessoa2 = input("Qual a sua idade: ")
peso_pessoa2 = input("Qual o seu peso: ")
altura_pessoa2 = input("Qual a sua altura: ")

nome_pessoa3 = input("Qual o seu nome: ")
idade_pessoa3 = input("Qual a sua idade: ")
peso_pessoa3 = input("Qual o seu peso: ")
altura_pessoa3 = input("Qual a sua altura: ")


texto = 'Meu nome é: {0:4}, minha idade é: {1:4}, meu peso é: {2:4}, minha altura é: {3:4}'
print(texto.format(nome_pessoa1,idade_pessoa1,peso_pessoa1,altura_pessoa1))
print(texto.format(nome_pessoa2,idade_pessoa2,peso_pessoa2,altura_pessoa2))
print(texto.format(nome_pessoa3,idade_pessoa3,peso_pessoa3,altura_pessoa3))
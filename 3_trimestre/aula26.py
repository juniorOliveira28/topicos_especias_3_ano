# este é um comentário
print("Olá Mundo :D") # exemplo de print
print
"""
Um comentário em bloco é definido com três áspas
Sejam elas simples ou duplasS
"""

# Variáveis não necessitam definição de tipo
num = 10;
num = "Junior"
num = 10.98

a = num * 10

# Jeito não preguiçoso
print("O resultado é", num, "certo?")

# O sinal {} representa o valor de uma Variável
print("O resultado é {}, certo?".format(num))

nome = "Junior"

print ("{}, o resultado é {}, certo?".format(nome, num))

# Operador de potênecessitam é **

num = 5 ** 2 # 5 ao quadrado
num = 5 ** 3
num = 10 ** 8 # 10 elevado a 8

# prioridade de operadores
# ** * / + -

num = 9 ** 1 / 2 # isso é 4,5
num = 9 ** (1/2) # isso é raiz = 3

num = 21

# Condicionais
if(num % 2 == 0 ): # finaloza com dois pontos
    print("O número {} é par".format(num))
    # coisas do if dever ficar identadas
    # ..
    if(True):
        print("Pertence ao if interno")

        while(True):
          print("Código do While!")

          break
        # Fim do while

    # Fim do IF interno

# Fim do IF externo
else:
    print("O número {} é impar!".format(num))

# Condicionais compostas:
# E --> && Em pyton é --> and
# || Em pyton é --> or

# Toda entrada do input é uma String
num = input("Digite um número: ")
# Conversão para int() ou float() é necessária
num = int(num)

i = 0
while (i <= 10):
    res = i * num
    print("{} X {} = {}".format(num, i, res))
    # Não existe i++ ou int
    # Acrescenta 1 ao valor de if
    i += 1 # é igual a i =1 + 1

# Listas, vetor, array
# Criando vetor vazio/nulo
vetor =[]

# Adicionando algo ao vetor
vetor.append(10)
vetor.append(3)
vetor.append(7)
vetor.append(8)


# Criando um vetor já preenchido
vetor =[10, 5, 19, 53, 48, 9]

# Criando vetor vazio com tamanho not
vetor = [""] * 10
vetor [0] = 19
vetor [1] = 5
vetor [9] = 12

# Pedindo para o usuário os valores...
vetor = [""] * 4

i = 0

# len() calcula o tamanho de algo
while(i < len(vetor)):
    vetor[i] = int (input("Número: "))

    # Incremento da  posição
    i = i + 1

    # Mostrando o vetor
    print(vetor)
    # Para fazer a soma
    soma = 0

    # Percorrendo  o vetor com o FOREACH
for x in vetor:
    print("O vetor tem o valor {}".format(x))

    soma = soma + x

print("A soma do vetor é {}".format(soma))

media = soma/len(vetor)

print("A média do vetor é {}".format(media))

#########################################################

# Funções e Classe

# Não precisa especificar tipo de parâmetro e de retorno
# def nome (parâmetro)
# ...
def somar(a, b, c):
    print(a+b+c)
    # O retorno é opcional
# Fim da Função

# Classe é a mesma coisa
class Aluno():
    nome = "Junior"

    def metodo():
        return ""

# class Nome(Herança)
# class Aluno(Pessoa):
    # A classe Aluno "extends" a classe Pessoa
    # Código da classe









































###

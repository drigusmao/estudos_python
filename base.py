#Aula Python Udemy professor Luiz Otávio Miranda.

print('Hello World!')
print('Tudo bem?')
print(12,34,45) #Três argumentos não nomeados.
print(23,34, sep='-', end='\n') #Mudei o separador que por via de regra é " " espaço simples agora é "-", depois coloquei o comando de barra de linha que ja é por padrão (não precisaria colocar).

"""
Isso é uma Docstring o interpretador do Python le mas não faz nada com elas (não ignora igual os comentários).

Python é uma linguagem de programação com tipagem Dinâmica (ja sabe o tipo da informação que passamos ex int,str,etc) e Forte. 

Python diferencia letras maiusculas e letras minusculas.

String (str) são textos entre aspas simples ou duplas.

Tipos numéricos int e float(com ponto flutuante .)
Podem ser negativos ou não, com "-" antes, sem sinal, é considerado positivo.
"""

print(type("oi")) #Lendo o tipo que foi perguntado ao Pyhton.

"""Tipo de dado boolean(só tem dois valores) ou é True ou é False.
Existem vários operadores para "questionar".
Por exemplo o ==, que é um operador lógico que questiona se um valor é igual ao outro.
"""

print(10 == 10) #Responde True ou seja sim é igual.
print(10 == 11) #False, não é igual.

#Convertendo um tipo em outro.
print(('1'), type('1'))
print(int(1.0)), type(int(1.0))
print(int(1.0) + 2) #Converti o 1.0 para 1 para podermos fazer as somas que precisam dos mesmos tipos ou tudo int ou tudo float.

print(str(11) + 'b') #Converti 11 para string para aparecer 11b.

nome = 'Adriana' #Atribui o nome Adriana a variavel nome.
print(nome) #Retornando o nome Adriana.
idade = 25 #Colocando a idade na variavel idade.

print('Nome:', nome) #Mostrando que o nome é Adriana.
print('Idade:', idade) #Mostrando que a idade é 25.

#Exercico do curso de variaveis e tipos de dados.

nome = 'Adriana'
sobrenome = 'Gusmão'
idade = 25
ano_de_nascimento = 2000
maior_de_idade = idade >= 18
altura_metros = 1.65

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_de_nascimento)
print('É maior de idade:', maior_de_idade)
print('Altura em metros:', altura_metros)

#Operadores aritméticos.

adicao = 10 + 10
print('Adição:', adicao)

subtracao = 10 - 5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2.2
print('Divisão: ', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira:', divisao_inteira) #Retorna um numero fluante com .0 cortando as casas decimais então pode não estar 100% correta.

exponenciacao = 2 ** 10
print('Exponenciação:', exponenciacao)

modulo = 25 % 5 #Retorna o resto da divisão(sobra).
print('Módulo: ', modulo)

#Concatenar strings sem misturar tipos, se quiser faça a conversão do tipo.
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

#Repetição de strings.
a_dez_vezes = 'A' * 10
tres_vezes_Adriana = 3 * 'Adriana'
print(a_dez_vezes)
print(tres_vezes_Adriana)

#Exercico cálculo de IMC.
nome = 'Adriana'
altura_metros = 1.65
peso_kg = 57
imc = peso_kg / (altura_metros * altura_metros)
print('Adriana seu IMC é:', int(imc))

#Printando a mesma coisa com f-strings
print(f'{nome} seu IMC é: {imc:.0f}') #Quantas casas decimais você quer? 2? então imc:.2f a formatação quantas casas decimais você quer é ':.3f'.

#Coletando informações do usuário e salvará então o nome digitado na variavel nome_usuario.
nome_usuario = input('Qual o seu nome? ') #O usuário poderá digitar seu nome após a pergunta que aparecerá na tela para ele.
print(f'{nome_usuario} muito obrigado pela informação!') #Mostra o nome digitado e agradece a informação.

#Pedindo a idade e transformando em numero inteiro e mostrando ela, se não converter fica salvo como string e então cáculos matematicos não serão feitos da melhor forma.
idade_usuario = int(input('Qual sua idade? '))
print(f'{nome_usuario} você tem {idade_usuario} anos!')



"""
If, elif e else são estruturas condicionais que permitem que o código execute diferentes blocos de instruções com base em condições específicas.

Vamos criar uma situação hipotética em que o usuário tem duas opções.

E então entre as duas opões usaremos estruturas condicionais como if, elif e else para o programa agir conforme a resposta dada pela usuário.
"""

#Vamos dar duas opções para o usuário
resposta_usuario = input('Você prefere o calor ou o frio? ')

#Vamos usar as estruturas condicionais para mandar uma mensagem conforme escolha do usuário.
if resposta_usuario == 'calor': #Primeira condição.
   print('Você prefere o calor!') #Esse espaço que demos antes do que executar se a condição for verdadeiro é uma identação, se não a fizer, dará erro. E todas identações devem permanecer com 4 espaços.
elif resposta_usuario == 'frio': #Segunda condição se não rodar a primeira.
   print('Você prefere o frio!')
else: #Se o usuário não responder nenhuma das opções acima aparecerá essa terceira opções de mensagem.
   print('Você não digitou nem calor nem frio.')

#Nenhuma dessas estruturas condicionais funciona sozinha: elif e else precisam do if, mas o if pode funcionar só com elif ou só com else.
#Posso colocar quantos elif eu quiser.

"""
Operadores de comparação (relacionais)

OP     Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

"""
Exercico utilizando os operadores de comparação e estruturas condicionais.
Solicite dois numeros ao usuário e depois peça para falar que numero é maior.
"""

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 > numero2:
   print(f'O numero {numero1} é maior do que o {numero2}.')
else:
   print(f'O {numero2} é maior do que o {numero1}.')

""" 
Operadores lógicos and (e) or (ou) not (não).

and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será falsa.

São considerados falsy (não são valores falsos mas são considerados falsos) = 0 ,  0.0,  '' , False.

Também existe o tipo None que é usado para representar um não valor.
"""

#Vamos dar duas opções ao nosso usuário.
entrada = input('Você quer entrar ou sair do programa: ')

#Solitando a senha para acesso ao programa.
senha_digitada = input('Digite sua senha: ')

#A senha do usuário é a seguinte.
senha_usuario = '123456'

if entrada == 'entrar' and senha_digitada == senha_usuario: #Só irá rodar o programa se as duas condições forem True.
    print('Entrada permitida ao usuário.')
else:
     print('Saída do programa.')

"""
or - Se uma condição for verdadeira considera toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

"""

#Vamos continuar a usar as variaveis do exercicio anterior para exempleficar o uso do 'or'
#Vamos supor que o usuario não escreveu a palavra entrar toda em minuscula mas usou a primeira letra maiuscula isso não pode impedi-lo de acessar o programa.

if (entrada == 'entrar' or 'Entrar') and senha_digitada == senha_usuario: #Só irá rodar o programa se uma das condições 'or' for True.
   print('Entrar')
else:
   print('Sair')

"""
not - Inverte expressões, o que for True vira False e o que for False vira True.

Operadores in e not in

Strings em Python são iteráveis (você pode navegar item por item usando seus indices ex Adriana pode navegar assim: A d r i a n a):
0 1 2 3 4 5
O t á v i o
-6-5-4-3-2-1

"""

nome = 'Adriana'

#Vamos acessar a letra i que está no indice 3 (começamos a contar do 0 ou seja a quantidade de elementos -1)
print(nome[3])

#Vamos ver se um x elemento está dentro da palavra Adriana
#A letra y está no nome Adriana? Se tiver ira aparecer True, se não aparecerá False.
print('y' in nome)

#Faça um programa que peça o nome do usuário e o que ele quer checar dentro do nome dele:

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

"""
Interpolação básica de strings (format de um jeito diferente)
s = string
d e i = int
f = float
x e X = Hexadecimal (ABCDEF0123456789) ('numeros' formados de letras do A ao E e numeros do 0 a 9)
"""

nome = 'Adriana'
preco = 25
variavel = 'Adriana, o preço total foi R$25.'
variavel_interpolaçao = '%s, o preço total foi R$%s' % (nome, preco) #Interpolação feita (coloco o %+s e depois coloco , e identifico na ordem o que é cada parte da interpolação).
print(variavel_interpolaçao)

"""
Formatação básica de strings.
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros.
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

#Exemplos
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #Fez uma largura fixa (preenche com espaços com 10 caracteres para esquerda alem do ABC que são 3 vai mais 7 para a esquerda).
print(f'{variavel: <10}.') #Largura fixa para direita
print(f'{variavel: ^10}.') #Faz largura fixa divindo na metade

"""
Fatiamento de strings (pega uma 'fatia' uma parte da sua 'string')

 Olá mundo
 012345678 #Posições na string acima
-987654321 #Negativos (do final para o começo)

"""

#Onde quero o fatimamento da string?
variavel = 'Olá mundo'
print(variavel[4:8]) #Coloco o começo do fatiamento  ':'  até o final +1 pq exclui um do indice final
#Se coloco :7 vai do começo até o indice 6
#Se coloco 3: vai do indice 3 até o final

print(len(variavel)) #A função len conta a quantidade de caracteres das strings

print(variavel[0:9:3]) #Lerá cada parte citada

#Exercicio: Pela ao usuario seu nome, sua idade e se forem digitados exiba o {nome}, (nome invertido), se tem ou não espaços, quantidade de letras, primeira letra do nome, a ultima e se nada for digitado em nome e idade exiba a mensagem "Desculpe, voce deixou campos vazios".

nome = (input('Digite seu nome: '))
idade = (input('Digite sua idade '))

if nome and idade:
  print(f'Seu nome é {nome}.')
  print(f'Seu nome invertido é {nome[::-1]}.')
  print(f'Seu nome tem {len(nome)} letras.')
  print(f'A primeira letra do seu nome é {nome[0]}.')
  print(f'A ultima letra do seu nome é {nome[-1]}.')
  if ' ' in nome:
    print('Seu nome tem espaços.')
  else:
    print('Seu nome não tem espaços.')
else:
  print('Desculpe, você deixou campos vazios.')
  




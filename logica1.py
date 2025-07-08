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






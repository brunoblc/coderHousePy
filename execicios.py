''' 1
conta matematica
'''

x = int(input("valor de x: "))
u = int(input("valor de u: "))
i = int(input("valor de i: "))

resultado = x + u * 18 + (u-i)/80

print(resultado)



''' 2

Desenvolva um código que receba uma variável alturaPessoa que guarda um
valor do tipo numérico (inteiro).

Caso a altura do usuário seja maior ou igual a 160cm, imprima na tela: ”Você
poderá pilotar o carro de F1!”

Se a altura for inferior a 160cm, imprima: “Você não tem a altura mínima para
pilotar esta máquina!”. 

Lembrando que só pode digirir depois dos 18 anos

'''

altura = float(input('Digite sua altura: \n' ))

idade = int(input('Digite sua idade: ' ))



if idade >= 18:

  if altura >= 1.60 :

    print('Você poderá pilotar o carro de F1!')

  else:

    print('Você não tem altura pilotar esta máquina!')

else:

  print('Você não tem idade para pilotar esta máquina!')


''' 3

Caso a temperatura esteja acima de 25 graus ou mais, imprima a frase: “Não
esqueça do filtro solar”

Para temperaturas entre 19 e 31, imprima: “Não esqueça seu óculos de sol”

para temperaturas abaixo de 19 imprima: “Já pegou seu casaco?”
'''

temperaturaAgora = int(input('Quantos graus está agora?: \n'))



if temperaturaAgora < 19:

  print('Já pegou seu casaco?')



else:

  if temperaturaAgora >= 19 and temperaturaAgora <= 31:

       print('Não esqueça seu óculos de sol')

       if temperaturaAgora >= 25:

            print('Não esqueça do filtro solar')
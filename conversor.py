opcao = input('1 - Real para Dolar\n2 - Dolar para real')
opcao = int(opcao)

valor = input('Digite o valor:')
valor = float(valor)

if opcao == 1:
    valor = valor / 4.38
    print('$',valor)
elif opcao == 2:
    valor = valor * 4.38
    print('R$',valor)
else:
    print('Opção inválida')

print('Fim da execução')

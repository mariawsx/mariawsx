def desenhar_casinha(tamanho):
 
    if tamanho < 3:
        print("O tamanho deve ser maior ou igual a 3.")
        return

  
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        barras = '\\' * (4 * i + 1)
        print(espacos + barras + espacos)

    largura = 4 * tamanho - 1
    for i in range(tamanho):
        if i == tamanho - 1:
            print('|' + ' ' * (largura - 2) + '|')
        else:
            print('|' + ' ' * (largura - 2) + '|')


    print('|' + '_' * (largura - 1) + '|')


tamanho = 10
desenhar_casinha(tamanho)

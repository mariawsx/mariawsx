def desenhar_casinha(tamanho):
    # Verifica se o tamanho é suficiente para desenhar uma casinha
    if tamanho < 3:
        print("O tamanho deve ser maior ou igual a 3.")
        return

    # Desenhar o telhado
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        barras = '\\' * (4 * i + 1)
        print(espacos + barras + espacos)

    # Desenhar as paredes e o teto
    largura = 4 * tamanho - 1
    for i in range(tamanho):
        if i == tamanho - 1:
            print('|' + ' ' * (largura - 2) + '|')
        else:
            print('|' + ' ' * (largura - 2) + '|')

    # Desenhar o chão
    print('|' + '_' * (largura - 1) + '|')

# Exemplo de uso
tamanho = 10
desenhar_casinha(tamanho)
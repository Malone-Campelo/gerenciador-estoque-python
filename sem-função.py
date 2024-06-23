from time import sleep

estoque = [
    { "produto": "Lapis", "quantidade": 2, "valor": 0.50 },
]

while True:
    print("""
    [ 1 ] Realizar Venda
    [ 2 ] Adicionar Produto
    [ 3 ] Atualizar Produto
    [ 4 ] Estoque
    [ 0 ] Sair
    """)
    escolha = input("Escolha a opção: ")
    
    if escolha == '1':
        print('')
        # ainda falta fazer a parte das vendas
        
        
    elif escolha == '2':
        while True:
            produto = input("Nome do produto (ou 'voltar' para encerrar): ")
            if produto.lower() == 'voltar':
                break
            quantidade = int(input('Qtd: '))
            preco = float(input('Valor R$: '))

            # Verificação e confirmação
            print(f'Produto: {produto}')
            print(f'Quantidade: {quantidade}')
            print(f'Valor: {preco:.2f}R$')
            confirmacao = input('As informações estão corretas? (s/n): ').lower()
            print('Aguarde...')
            sleep(2)

            if confirmacao == 's':
                if quantidade > 0 and preco > 0:
                    estoque.append({'produto': produto, 'quantidade': quantidade, 'valor': preco})
                    print('Adicionado com sucesso!')
                else:
                    print('ERRO: quantidade ou preço inválido!')
            else:
                print('Operação cancelada.')
            break
    
    elif escolha == '3':
        while True:
            produto = input("Nome do produto (ou 'voltar' para cancelar): ")
            if produto.lower() == 'voltar':
                break
            quantidade = int(input('Qtd: '))
            preco = float(input('Preço: '))

            # Verificação e confirmação
            print(f'Produto: {produto}')
            print(f'Quantidade: {quantidade}')
            print(f'Valor: {preco:.2f}R$')
            confirmacao = input('As informações estão corretas? (s/n): ').lower()
            print('Aguarde...')
            sleep(2)

            if confirmacao == "s":
                if quantidade == 0 and preco == 0:
                    produto_encontrado = False
                    for item in estoque:
                        if item['produto'].lower() == produto.lower():
                            item['quantidade'] = quantidade
                            item['valor'] = preco
                            produto_encontrado = True
                            print('Atualizado com sucesso!')
                            break
                    if not produto_encontrado:
                        print('Produto não encontrado no estoque.')
                else:
                    print('ERRO, quantidade ou valor incorreto.')
            else:
                print('Operação cancelada.')
            break
    
    elif escolha == '4':
        # Exibir estoque
        print('\nEstoque atual:')
        for item in estoque:
            print(f"Produto: {item['produto']} | Quantidade: {item['quantidade']} | Valor: {item['valor']:.2f}R$")
        input('\nPrecione Enter para voltar ao menu...')
    
    elif escolha == '0':
        print('Saindo do sistema...')
        sleep(1)
        break
    
    else:
        print('Opção inválida. Tente novamente.')

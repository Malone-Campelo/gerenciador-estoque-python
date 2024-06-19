# Lista
estoque = [
    { "produto": "Lapis", "quantidade": 0, "valor": 0.50 },
]
# Função para adicionar, nome produto, quantidade e valor
def adicionar_produto(estoque):
    produto = input("Inserir produto: ")
    quantidade = int(input("Qtd: "))
    preco = float(input("Valor R$: "))
    
    # Verificação e confirmação
    print(f"\nConfirme as informações:")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: {preco:.2f}R$")
    confirmacao = input("As informações estão corretas: s/n").lower()
   
    if confirmacao == "s":
        if quantidade > 0 and preco > 0:
            estoque.append({"produto": produto, "quantidade": quantidade, "valor": preco})
            print("Adicionado com sucesso!")
        else:
            print("ERRO: quantidade inválida! ")
    else:
        print("Operação cancelada.")
        
            
def atualizar_estoque(estoque):
    produto = input("Qual produto deseja ajustar: ")
    quantidade = int("Qtd: ")
    preco = float("Preço: ")
    
    # Verificar e confirmar
    print(f"\nConfirme as informações:")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: {preco:.2f}R$")
    
    confirmacao = input("As informações estão corretas? (s/n): ").lower()
    if confirmacao == 's':
        if quantidade >= 0 and preco >= 0:
            print

    
print("""
[ 1 ] Adicionar Produto
[ 2 ] Atualizar Produto
[ 3 ] Estoque
[ 4 ] Sair
""")

while True:
    escolha = (input("Escolha a opção: "))
    
    if escolha == '1':
        print("Adicionar produto")
    elif escolha == '2':
        print("Atualizar produto")
    elif escolha == '3':
        estoque.lenght
    elif escolha == '4':
        print("Saindo dos sistema")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
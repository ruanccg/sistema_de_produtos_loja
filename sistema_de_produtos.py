# ============================================================
#                   SISTEMA DE PRODUTOS
# ============================================================

codigos = [] # Essa lista irá armazenar os códigos dos produtos como inteiro
nomes = []  # Essa lista irá armazenar os nomes dos produtos como string
precos = [] # Essa lista irá armazenar os preços dos produtos como float
quantidades = [] # Essa lista irá armazenar as quantidades dos produtos como inteiro

ARQUIVO = "produtos_com_dados.csv" #Aqui criamos uma variável que irá armazenar o documento externo que contém os produtos em estoque

def carregar_produtos(): #Aqui vamos abrir a função para carregar produtos e salvar dentro do arquivo externo
    try: # Inserimos o Try para executar o código que pode dar erro
        f = open(ARQUIVO, "r", encoding="utf-8") # Aqui usamos a função open para abrir o arquivo e ler, usamos também o encoding para compreender as acentuações
        for linha in f: # Aqui o laço for irá percorrer linha por linha dentro do arquivo
            linha = linha.replace("\n", "") # Aqui removemos o caractere de espaço no final de cada linha
            if linha == "": # Aqui nesta condicional IF, se a linha estiver vazia, ele pula para a próxima
                continue

            partes = linha.split(";") # Aqui decidimos separar a linha em 4 partes usando ';' como separador
            if len(partes) != 4: # Se não tiver 4 partes, arquivo errado, ignora a linha
                continue

            codigos.append(int(partes[0])) # Aqui é realizado a conversão e inserção dos códigos ao documento
            nomes.append(partes[1]) # # Aqui é realizado a conversão e inserção dos nomes ao documento
            precos.append(float(partes[2])) # Aqui é realizado a conversão e inserção dos preços ao documento
            quantidades.append(int(partes[3])) # Aqui é realizado a conversão e inserção das quantidades ao documento

        f.close() # Aqui fechamos o documento 
        print(len(codigos), "produto(s) carregado(s).") # Aqui mostra quantos produtos existem dentro do arquivo

    except FileNotFoundError: # # Se o arquivo não existir, é mostrado a mensagem de erro
        print("Arquivo não encontrado. Sistema iniciará vazio.")


def salvar_produtos(): # Função para salvar todas as listas no documento
    f = open(ARQUIVO, "w", encoding="utf-8") # Aqui usamos a função open para abrir o arquivo e ler, usamos também o encoding para compreender as acentuações
    i = 0 # Aqui iniciamos o indíce em 0
    while i < len(codigos): # Enquanto houver itens na lista, ele executa o código a seguir
        linha = str(codigos[i]) + ";" + nomes[i] + ";" + str(precos[i]) + ";" + str(quantidades[i]) + "\n"
        f.write(linha)
        i = i + 1
    f.close() # Aqui fechamos o documento
    print("Produtos salvos no arquivo.")


# ============================================================
#                    FUNÇÕES DE APOIO
# ============================================================
def ler_inteiro(msg): # Aqui criamos uma função para evitar erros de inserção de float
    valor = input(msg) 
    while valor.isdigit() == False: # Aqui usamos o isdigit que verifica se todos os caracteres são números
        print("Digite um número inteiro válido!")
        valor = input(msg)
    return int(valor) # Aqui converte o valor para inteiro e retorna


def ler_float(msg): # Aqui criamos também uma função para evitar erros de inserção de inteiros
    valor = input(msg)
    valido = False # Começamos com a variável recebendo valor FALSE

    while valido == False: # Enquanto a variável receber valor FALSE, vai executar o código
        valido = True
        pontos = 0

        for caracter in valor: # Aqui ele vai percorrer cada caractere dentro da variável VALOR
            if caracter == ".": # Se houver um ponto, ocorre o incremento
                pontos += 1
                if pontos > 1: # Se houver mais de um ponto, é inválido
                    valido = False
            elif caracter.isdigit() == False: # Se não for número e nem ponto, se torna inválido também
                valido = False

        if valor == "": # Se o valor for vazio, é inválido
            valido = False

        if valido == False: # E se o valor for False, ele vai solicitar novamente ao usuário a inserção
            print("Digite um número válido (ex: 10 ou 10.50):")
            valor = input(msg)

    return float(valor) # Converte para float e retorna


# ============================================================
#                     CRUD DE PRODUTOS
# ============================================================
def cadastrar_produto(): # Aqui criamos a função responsável pelo cadastro de produtos
    print("\n=== CADASTRAR PRODUTO ===") 

    codigo = ler_inteiro("Código do produto: ") # Aqui usamos a função ler_inteiro para verificar o código do produto inserido pelo usuário

    if codigo in codigos: # Se o código digitado já estiver contido dentro da variável, mostra erro, e solicita novamente a inserção para o usuário
        print("ERRO: já existe produto com esse código!")
        return

    nome = input("Nome do produto: ") # Aqui solicitamos a inserção do nome do produto
    while nome == "": # Se o nome estiver vazio, mostra erro, e solicita novamente
        print("Nome não pode ser vazio!")
        nome = input("Nome do produto: ")

    preco = ler_float("Preço: ") # Aqui solicitamos o preço e fazemos a verificação do preço com a função ler_float

    quantidade = ler_inteiro("Quantidade em estoque: ") # Aqui solicitamos a quantidade e fazemos a verificação da quantidade com a função ler_inteiro

    if quantidade < 0: # Se quantidade for menor que 0, mostrar erro
        print("ERRO: quantidade não pode ser negativa!")
        return

    # Aqui inserimos os valores dentro de suas respectivas listas
    codigos.append(codigo) 
    nomes.append(nome)
    precos.append(preco)
    quantidades.append(quantidade)

    salvar_produtos() # Aqui salvamos as informações dentro do arquivo CSV.
    print("Produto cadastrado com sucesso!")


def listar_produtos(): # Aqui criamos a função para listar produtos
    print("\n=== LISTAGEM DE PRODUTOS ===")

    if len(codigos) == 0: # Se a quantidade de códigos dentro da variável for igual a 0, mostrar a mensagem abaixo
        print("Nenhum produto cadastrado.")
        return

    i = 0 # Iniciamos o índice com 0
    while i < len(codigos): # Enquanto o índice for menor que a quantidade de produtos, mostra a lista de produtos
        print(
            "Código:", codigos[i],
            "| Nome:", nomes[i],
            "| Preço: R$", round(precos[i], 2), # Esse ROUND mostra o preço com duas casas decimais
            "| Quantidade:", quantidades[i]
        )
        i = i + 1 # Ocorre o incremento


def buscar_produto(): # Aqui criamos a função Buscar Produto
    print("\n=== BUSCAR PRODUTO ===")

    codigo = ler_inteiro("Código do produto: ")

    i = 0 
    while i < len(codigos):
        if codigos[i] == codigo:
            print("Encontrado!")
            print("Código:", codigos[i],
                  "| Nome:", nomes[i],
                  "| Preço: R$", round(precos[i], 2),
                  "| Quantidade:", quantidades[i])
            return
        i = i + 1

    print("Produto NÃO encontrado.")


def atualizar_produto(): # Aqui criamos a função para atualizar alguma informação do produto
    print("\n=== ATUALIZAR PRODUTO ===")

    codigo = ler_inteiro("Digite o código do produto: ")

    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:

            print("Produto atual:")
            print("Nome:", nomes[i])
            print("Preço: R$", round(precos[i], 2))
            print("Quantidade:", quantidades[i])

            novo_nome = input("Novo nome (enter mantém): ")
            if novo_nome != "":
                nomes[i] = novo_nome

            novo_preco = input("Novo preço (enter mantém): ")
            if novo_preco != "":
                # validar preço manualmente, como a validação da função ler_float
                valido = False
                while valido == False:
                    valor = novo_preco
                    valido = True
                    pontos = 0
                    for caracter in valor:
                        if caracter == ".":
                            pontos = pontos + 1
                            if pontos > 1:
                                valido = False
                        elif caracter.isdigit() == False:
                            valido = False
                    if valor == "":
                        valido = False
                    if valido == False:
                        print("Preço inválido!")
                        novo_preco = input("Novo preço (enter mantém): ")
                precos[i] = float(novo_preco)

            nova_quantidade = input("Nova quantidade (enter mantém): ")
            if nova_quantidade != "":
                while nova_quantidade.isdigit() == False:
                    print("Quantidade inválida!")
                    nova_quantidade = input("Nova quantidade: ")
                quantidades[i] = int(nova_quantidade)

            salvar_produtos() # Aqui executamos novamente a função para salvar os valores dentro do documento
            print("Produto atualizado com sucesso!")
            return

        i = i + 1

    print("Produto não encontrado.")


def remover_produto(): # Aqui criamos a função para remover um produto
    print("\n=== REMOVER PRODUTO ===")

    codigo = ler_inteiro("Código do produto a remover: ")

    i = 0
    while i < len(codigos):
        if codigos[i] == codigo: # Ele vai percorrer índice por índice até encontrar o produto
            del codigos[i] #Com DEL removemos todos os dados dos produtos juntos!
            del nomes[i]
            del precos[i]
            del quantidades[i]
            salvar_produtos()
            print("Produto removido com sucesso!")
            return
        i = i + 1

    print("Produto não encontrado.")


# ============================================================
#                        RELATÓRIOS
# ============================================================
def relatorio_estoque_baixo(): # Aqui criamos o primeiro relatório solicitado pelo professor
    print("\n=== RELATÓRIO: ESTOQUE BAIXO ===")

    limite = ler_inteiro("Listar produtos com quantidade <= ")

    caminho = "arquivos_csv_relatorios/relatorio_estoque_baixo.txt" # Aqui nós pedimos para ele criar um arquivo txt com o relatório que solicitamos
    f = open(caminho, "w", encoding="utf-8") # Aqui usamos a função open para abrir o arquivo e escrever, usamos também o encoding para compreender as acentuações

    f.write("RELATÓRIO: ESTOQUE BAIXO\n") # Cabeçalho no TXT
    f.write("Quantidade menor ou igual a: " + str(limite) + "\n\n") # Info do resultado do relatório

    achou = False
    i = 0
    while i < len(codigos): # Aqui vai percorrer todos os produtos, índice por índice
        if quantidades[i] <= limite: # Se quantidades estiver menor ou igual ao limite, executa abaixo
            linha = (
                "Código: " + str(codigos[i]) +
                " | Nome: " + nomes[i] +
                " | Quantidade: " + str(quantidades[i]) + "\n"
            )
            print(linha, end="") # Aqui finaliza o texto sem linha extra
            f.write(linha) # Aqui vai escrever no documento
            achou = True # Aqui marca que encontrou 
        i += 1

    if achou == False: # Se a variável igual a FALSE, aí mostra a mensagem abaixo para o usuário dentro do documento
        print("Nenhum produto com estoque baixo.")
        f.write("Nenhum produto com estoque baixo.\n")

    f.close() # Aqui fechamos o documento
    print("\nRelatório salvo em:", caminho)


def relatorio_ordenar_por_preco(): # Aqui criamos o segundo relatório solicitado pelo professor
    print("\n=== RELATÓRIO: PRODUTOS ORDENADOS POR PREÇO ===")

    if len(codigos) == 0: 
        print("Nenhum produto cadastrado.")
        return

    # Aqui vamos fazer a comparação dos preços usando método Bubble Sort
    n = len(codigos) # Aqui listamos a quantidade de produtos
    i = 0 # Aqui iniciamos o índice com 0
    while i < n - 1: # Aqui ele vai realizar o processo de comparação enquanto o índice for menor que n - 1
        j = 0 
        while j < n - 1 - i:
            if precos[j + 1] < precos[j]: # Se o preço do próximo produto é menor do que o preço do atual, ele troca!

                # Aqui usamos variáveis temporárias para guardar o valor antigo antes de fazer a troca.
                codigo_temporario = codigos[j] 
                codigos[j] = codigos[j + 1]
                codigos[j + 1] = codigo_temporario

                nome_temporario = nomes[j]
                nomes[j] = nomes[j + 1]
                nomes[j + 1] = nome_temporario

                precos_temporario = precos[j]
                precos[j] = precos[j + 1]
                precos[j + 1] = precos_temporario

                quantidades_temporaria = quantidades[j]
                quantidades[j] = quantidades[j + 1]
                quantidades[j + 1] = quantidades_temporaria

            j += 1
        i += 1

    caminho = "arquivos_csv_relatorios/relatorio_ordenado_preco.txt" # Aqui nós pedimos para ele criar um arquivo txt com o relatório que solicitamos
    f = open(caminho, "w", encoding="utf-8") # Abre arquivo para escrita
    f.write("RELATÓRIO: PRODUTOS ORDENADOS POR PREÇO\n\n") # Aqui é o cabeçalho do documento

    i = 0
    while i < len(codigos): # Percorre as listas já ordenadas
        linha = (
            "Código: " + str(codigos[i]) +
            " | Nome: " + nomes[i] +
            " | Preço: R$" + str(round(precos[i], 2)) +
            " | Quantidade: " + str(quantidades[i]) + "\n"
        )
        print(linha, end="")
        f.write(linha)
        i += 1

    f.close() # Fecha o arquivo de relatório
    print("\nRelatório salvo em:", caminho)


def relatorio_total_itens(): # Aqui criamos o terceiro relatório solicitado pelo professor
    print("\n=== RELATÓRIO: TOTAL DE ITENS EM ESTOQUE ===")

    total = 0
    i = 0
    while i < len(quantidades): # Enquanto índice for menos que a quantidade de cada produto, execute abaixo
        total = total + quantidades[i] 
        i += 1 # Aqui ocorre o incremento

    print("Total de itens no estoque:", total) # Mostra o total de itens dentro do documento

    caminho = "arquivos_csv_relatorios/relatorio_total_itens.txt"
    f = open(caminho, "w", encoding="utf-8") # Abre arquivo para escrita
    f.write("RELATÓRIO: TOTAL DE ITENS EM ESTOQUE\n\n") # Cabeçalho do documento
    f.write("Total de itens: " + str(total) + "\n") 
    f.close() # Fecha o documento

    print("\nRelatório salvo em:", caminho)

# ============================================================
#                      MENU PRINCIPAL
# ============================================================
def menu(): #Aqui criamos a função que sempre mostrará o menu do sistema de produtos
    while True: # Aqui criamos um loop infinito com WHILE até o usuário escolher sair (opção "0")
        print("\n===== SISTEMA DE LOJA =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("6 - Relatório: estoque baixo")
        print("7 - Relatório: ordenar por preço")
        print("8 - Relatório: total de itens em estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ") # Aqui pedimos para o usuário escolher uma opção

        if opcao == "1":
            cadastrar_produto() # Função Cadastrar novo produto
        elif opcao == "2":
            listar_produtos() # Função Listar Produtos
        elif opcao == "3":
            buscar_produto() # Função Buscar Produto
        elif opcao == "4":
            atualizar_produto() # Função Atualizar porduto
        elif opcao == "5":
            remover_produto() # Função Remover Produto
        elif opcao == "6":
            relatorio_estoque_baixo() # Função Gerar relatório estoque baixo
        elif opcao == "7":
            relatorio_ordenar_por_preco() # Função Gerar relatório ordenado por preço
        elif opcao == "8":
            relatorio_total_itens() # Função Gerar relatório total de itens
        elif opcao == "0":
            print("Saindo do sistema...")
            break # Encerra o loop e sai
        else:
            print("Opção inválida! Tente novamente.")


# ============================================================
#                    PROGRAMA PRINCIPAL
# ============================================================
carregar_produtos()  # Ao iniciar, carregamos produtos do documento
menu() # Em seguida, mostramos o menu e começamos a interagir com o usuário

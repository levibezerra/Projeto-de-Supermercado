def menu():
    print('Menu Inicial:\n1 - Listar produtos\n2 - Adicionar produto ao carrinho\n3 - Ver carrinho\n4 - Finalizar compra')

def listar_produtos():
    produtos = '''
Frutas e Verduras:

1 – Maça - R$4,00 kg
2 – Tomate - R$6,00 kg
3 – Alface - R$2,00 kg
4 – Cenoura - R$3,00 kg
5 – Cebola - R$3,50 kg
6 – Uva - R$4,50 kg
7 – Limao - R$4,80 kg
8 – Coentro - R$1,00 kg
9 – Banana - R$5,00 kg
10 – Mamão - R$6,20 kg

Produtos de Limpeza:

11 – Amaciante – R$10,00
12 – Detergente – R$8,00
13 – Desinfetante – R$7,50
14 – Sabão em pó – R$5,30
15 – Sabão em barra – R$2,40
16 – Sabão líquido – R$8,30
17 – Água Sanitaria – R$3,00
18 – Limpa Vidros – R$11,00
19 – Multiuso – R$5,20
20 – Alvejante – R$12,00

Molhos:

21 – Molho de Tomate – R$7,30
22 – Extrato de Tomate – R$8,30
23 – Molho Shoyo – R$10,40
24 – Molho Caesar – R$18,00
25 – Molho Barbacue – R$17,50
26 – Molho Rosé – R$18,70
27 – Molho Quatro Queijos - R$20,30
28 – Molho bechamel – R$20,30
29 – Molho italiano – R$21,80
30 – Molho balsâmico – R$10,20

Alimentos:

31 – Arroz – R$9,00
32 – Feijão – R$8,00
33 – Macarrão espaguete – R$5,00
34 – Macarrão parafuso – R$5,40
35 – Farinha de trigo – R$3,50
36 – Massa para cuscuz – R$2,30
37 – Massa para tapioca – R$4,80
38 – Açúcar – R$10,10
39 – Sal – R$3,00
40 – Café – R$9,70

Higiene Pessoal:

41 – Shampoo – R$29,00
42 – Condicionador – R$32,00
43 – Sabonete – R$5,00
44 – Pasta de dente – R$2,50
45 – Escova de dente – R$5,40
46 – Fio dental – R$1,30
47 – Desodorante – R$20,10
48 – Creme de cabelo – R$25,40
49 – Absorvente – R$30,30
50 – Sabonete líquido – R$34,80

Bebidas:

51 – Agua – R$4,00
52 – Cerveja – R$6,80
53 – Refrigerante – R$8,00
54 – Suco – R$11,00
55 – Vinho – R$63,00
56 – Whisky – R$100,00
57 – Cachaça – R$40,00
58 – Vodka – R$75, 00
59 – Rum – R$40,00
60 – Espumante – R$80,00
    '''
    return produtos

def adicionar_produto(carrinho1,matriz1,compra):
    valor = 0
    lista = []
    numero = int(input('Informe o numero do produto: '))
    quant = int(input('Informe a quantidade que deseja comprar do produto: '))
    lista = matriz1[numero - 1]
    produto = lista[0]
    preco = lista[1]
    carrinho1.append(produto)
    carrinho1.append(quant)
    carrinho1.append(preco)
    valor = quant * preco
    compra += valor
    return compra

def ver_carrinho(carrinho1):
    print('Carrainho : ', carrinho1)

def finalizar_compra():
    return 4

matriz = [['Maça', 4.0], ['Tomate', 6.0], ['Alface', 2.0], ['Cenoura', 3.0],
          ['Cebola', 3.5], ['Uva', 4.5], ['Limao', 4.8], ['Coentro', 1.0],
          ['Banana', 5.0], ['Mamão', 6.2], ['Amaciante', 10.0], ['Detergente', 8.0],
          ['Desinfetante', 7.5], ['Sabão em pó', 5.3], ['Sabão em barra', 2.4],
          ['Sabão líquido', 8.3], ['Água Sanitaria', 3.0], ['Limpa Vidros', 11.0],
          ['Multiuso', 5.2], ['Alvejante', 12.0], ['Molho de Tomate', 7.3],
          ['Extrato de Tomate', 8.3], ['Molho Shoyo', 10.4], ['Molho Caesar', 18.0],
          ['Molho Barbacue', 17.5], ['Molho Rosé', 18.7], ['Molho Quatro Queijos', 20.3],
          ['Molho bechamel', 20.3], ['Molho italiano', 21.8], ['Molho balsâmico', 10.2],
          ['Arroz', 9.0], ['Feijão', 8.0], ['Macarrão espaguete', 5.0], ['Macarrão parafuso', 5.4],
          ['Farinha de trigo', 3.5], ['Massa para cuscuz', 2.3], [' Massa para tapioca', 4.8],
          ['Açúcar', 10.1], ['Sal', 3.0], ['Café', 9.7], ['Shampoo', 29.0], ['Condicionador', 32.0],
          ['Sabonete', 5.0], ['Pasta de dente', 2.5], ['Escova de dente', 5.4], ['Fio dental', 1.3],
          ['Desodorante', 20.1], ['Creme de cabelo', 25.4], ['Absorvente', 30.3], ['Sabonete líquido', 34.8],
          ['Água', 4.0], ['Cerveja', 6.8], ['Refrigerante', 8.0], ['Suco', 11.0], ['Vinho', 63.0], ['Whisky', 100.0],
          ['Cachaça', 40.0], ['Vodka', 75.0], ['Rum', 40.0], ['Espumante', 80.0]]

carrinho = []
compra = 0
valor_final = 0
cont = ''

while cont != 4:
    menu()
    var = int(input('Digite o código para prosseguir: '))
    print('')

    if var == 1:
       print(listar_produtos())

    elif var == 2:
        valor_final += adicionar_produto(carrinho, matriz, compra)

    elif var == 3:
        ver_carrinho(carrinho)

    elif var == 4:
        cont = finalizar_compra()

print(f'O valor final da compra é: R${valor_final:.2f}')
print('Fim!')

cont = ''
var = 0
valor_final = 0
lista_produtos = ['Maça', 'Tomate', 'Alface', 'Cenoura', 'Cebola', 'Uva', 'Limao', 'Coentro', 'Banana', 'Mamão',
                  'Amaciante', 'Detergente', 'Desinfetante', 'Sabão em pó', 'Sabão em barra', 'Sabão líquido',
                  'Água Sanitaria', 'Limpa Vidros', 'Multiuso', 'Alvejante', 'Molho de Tomate', 'Extrato de Tomate',
                  'Molho Shoyo', 'Molho Caesar', 'Molho Barbacue', 'Molho Rosé', 'Molho Quatro Queijos', 'Molho bechamel',
                  'Molho italiano', 'Molho balsâmico', 'Arroz', 'Feijão', 'Macarrão espaguete', 'Macarrão parafuso',
                  'Farinha de trigo', 'Massa para cuscuz', ' Massa para tapioca', 'Açúcar', 'Sal', 'Café', 'Shampoo',
                  'Condicionador', 'Sabonete', 'Pasta de dente', 'Escova de dente', 'Fio dental', 'Desodorante',
                  'Creme de cabelo', 'Absorvente', 'Sabonete líquido', 'Água', 'Cerveja', 'Refrigerante', 'Suco', 'Vinho',
                  'Whisky', 'Cachaça', 'Vodka', 'Rum', 'Espumante']

lista_valores = [4.00, 6.00, 2.00, 3.00, 3.50, 4.50, 4.80, 1.00, 5.00, 6.20, 10.00, 8.00, 7.50, 5.30, 2.40, 8.30, 3.00,
                 11.00, 5.20, 12.00, 7.30, 8.30, 10.40, 18.00, 17.50, 18.70, 20.30, 20.30, 21.80, 10.20, 9.00, 8.00, 5.00,
                 5.40, 3.50, 2.30, 4.80, 10.10, 3.00, 9.70, 29.00, 32.00, 5.00, 2.50, 5.40, 1.30, 20.10, 25.40, 30.30,
                 34.80, 4.00, 6.80, 8.00, 11.00, 63.00, 100.00, 40.00, 75.00, 40.00, 80.00]
lista = []
while var != 4 and cont != 4:
    while cont == '':
        print('Menu Inicial:\n1 - Listar produtos\n2 - Adicionar produto ao carrinho\n3 - Ver carrinho\n4 - Finalizar compra')
        var = int(input('Digite o codigo para prosseguir: '))
        print('')
        if var == 1:
            print('Frutas e Verduras:')
            print('')
            print('1 – Maça - R$4,00 kg\n2 – Tomate - R$6,00 kg\n3 – Alface - R$2,00 kg\n4 – Cenoura - R$3,00 kg\n5 – Cebola - R$3,50 kg\n6 – Uva - R$4,50 kg')
            print('7 – Limao - R$4,80 kg\n8 – Coentro - R$1,00 kg\n9 – Banana - R$5,00 kg\n10 – Mamão - R$6,20 kg')
            print('')
            print('Produtos de Limpeza:')
            print('')
            print('11 – Amaciante – R$10,00\n12 – Detergente – R$8,00\n13 – Desinfetante – R$7,50\n14 – Sabão em pó – R$5,30\n15 – Sabão em barra – R$2,40')
            print('16 – Sabão líquido – R$8,30\n17 – Água Sanitaria – R$3,00\n18 – Limpa Vidros – R$11,00\n19 – Multiuso – R$5,20\n20 – Alvejante – R$12,00')
            print('')
            print('Molhos')
            print('')
            print('21 – Molho de Tomate – R$7,30\n22 – Extrato de Tomate – R$8,30\n23 – Molho Shoyo – R$10,40\n24 – Molho Caesar – R$18,00')
            print('25 – Molho Barbacue – R$17,50\n26 – Molho Rosé – R$18,70\n27 – Molho Quatro Queijos - R$20,30\n28 – Molho bechamel – R$20,30')
            print('29 – Molho italiano – R$21,80\n30 – Molho balsâmico – R$10,20')
            print('')
            print('Alimentos:')
            print('')
            print('31 – Arroz – R$9,00\n32 – Feijão – R$8,00\n33 – Macarrão espaguete – R$5,00\n34 – Macarrão parafuso – R$5,40\n35 – Farinha de trigo – R$3,50')
            print('36 – Massa para cuscuz – R$2,30\n37 – Massa para tapioca – R$4,80\n38 – Açúcar – R$10,10\n39 – Sal – R$3,00\n40 – Café – R$9,70')
            print('')
            print('Higiene Pessoal:')
            print('')
            print('41 – Shampoo – R$29,00\n42 – Condicionador – R$32,00\n43 – Sabonete – R$5,00\n44 – Pasta de dente – R$2,50\n45 – Escova de dente – R$5,40')
            print('46 – Fio dental – R$1,30\n47 – Desodorante – R$20,10\n48 – Creme de cabelo – R$25,40\n49 – Absorvente – R$30,30\n50 – Sabonete líquido – R$34,80')
            print('')
            print('Bebidas:')
            print('')
            print('51 – Agua – R$4,00\n52 – Cerveja – R$6,80\n53 – Refrigerante – R$8,00\n54 – Suco – R$11,00\n55 – Vinho – R$63,00\n56 – Whisky – R$100,00')
            print('57 – Cachaça – R$40,00\n58 – Vodka – R$75, 00\n59 – Rum – R$40,00\n60 – Espumante – R$80,00')
            print('')
        if var == 2:
            numero = int(input('Informe o numero do produto: '))
            quant = int(input('Informe a quantidade que deseja comprar do produto: '))
            lista.append(lista_produtos[numero - 1])
            lista.append(quant)
            lista.append(lista_valores[numero - 1])
            soma = lista_valores[numero - 1]
            valor = soma * quant
            valor_final += valor
        elif var == 3:
            print('Carrinho =', lista)
        if var == 4:
            cont = 4
        else:
            cont = input('')
if var == 4:
    print(f'O valor final da compra é: R${valor_final:.2f}')
print('Fim!')


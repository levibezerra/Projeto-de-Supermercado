cont = ''
cont1 = ''
var = int(input('Digite o codigo para prosseguir: '))
print('1 - Listar produtos')
print('2- adicionar produto ao carrinho')
print('3 - ver carrinho')
print('4 - finalizar compra')
while cont != '4':
    print(var)
    cont = int(input('Digite o codigo para prosseguir: '))
    if var == 1:
        print('Supermercado Compre Mais.')
        print('Lista de Produtos:')
        print('1 – Frutas e Verduras')
        print('2 – Produtos de Limpeza')
        print('3 – Molhos')
        print('4 – Alimentos')
        print('5 – Higiene Pessoal')
        print('6 – Bebidas')
    cont = input('')
    while cont1 == '':
        cod = int(input('Digite um codigo do menu: '))
        if cod == 1:
            print('1 – Maça - R$4,00 kg')
            print('2 – Tomate - R$6,00 kg')
            print('3 – Alface - R$2,00 kg')
            print('4 – Cenoura - R$3,00 kg')
            print('5 – Cebola - R$3,50 kg')
            print('6 – Uva - R$4,50 kg')
            print('7 – Limao - R$4,80 kg')
            print('8 – Coentro - R$1,00 kg')
            print('9 – Banana - R$5,00 kg')
            print('10 – Mamão - R$6,20 kg')
        elif cod == 2:
            print('11 – Amaciante – R$10,00')
            print('12 – Detergente – R$8,00')
            print('13 – Desinfetante – R$7,50')
            print('14 – Sabão em pó – R$5,30')
            print('15 – Sabão em barra – R$2,40')
            print('16 – Sabão líquido – R$8,30')
            print('17 – Água Sanitaria – R$3,00')
            print('18 – Limpa Vidros – R$11,00')
            print('19 – Multiuso – R$5,20')
            print('20 – Alvejante – R$12,00')
        elif cod == 3:
            print('21 – Molho de Tomate – R$7,30')
            print('22 – Extrato de Tomate – R$8,30')
            print('23 – Molho Shoyo – R$10,40')
            print('24 – Molho Caesar – R$18,00')
            print('25 – Molho Barbacue – R$17,50')
            print('26 – Molho Rosé – R$18,70')
            print('27 – Molho Quatro Queijos - R$20,30')
            print('28 – Molho bechamel – R$20,30')
            print('29 – Molho italiano – R$21,80')
            print('30 – Molho balsâmico – R$10,20')
        elif cod == 4:
            print('31 – Arroz – R$9,00')
            print('32 – Feijão – R$8,00')
            print('33 – Macarrão espaguete – R$5,00')
            print('34 – Macarrão parafuso – R$5,40')
            print('35 – Farinha de trigo – R$3,50')
            print('36 – Massa para cuscuz – R$2,30')
            print('37 – Massa para tapioca – R$4,80')
            print('38 – Açúcar – R$10,10')
            print('39 – Sal – R$3,00')
            print('40 – Café – R$9,70')
        elif cod == 5:
            print('41 – Shampoo – R$29,00')
            print('42 – Condicionador – R$32,00')
            print('43 – Sabonete – R$5,00')
            print('44 – Pasta de dente – R$2,50')
            print('45 – Escova de dente – R$5,40')
            print('46 – Fio dental – R$1,30')
            print('47 – Desodorante – R$20,10')
            print('48 – Creme de cabelo – R$25,40')
            print('49 – Absorvente – R$30,30')
            print('50 – Sabonete líquido – R$34,80')
        elif cod == 6:
            print('51 – Agua – R$4,00')
            print('52 – Cerveja – R$6,80')
            print('53 – Refrigerante – R$8,00')
            print('54 – Suco – R$11,00')
            print('55 – Vinho – R$63,00')
            print('56 – Whisky – R$100,00')
            print('57 – Cachaça – R$40,00')
            print('58 – Vodka – R$75, 00')
            print('59 – Rum – R$40,00')
            print('60 – Espumante – R$80,00')
        else:
            print('Codigo Invalido')
        cont1 = input('')


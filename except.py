import os
os.system ('cls')
cantem = 0
cantea = 0
canteam = 0
cantemD = 0
canteaD = 0
canteamD = 0
menuprecio = ('''
Club de deportes "BUENA AVENTURA"

    N°|Entradas|Precio
    ------------------
    1 |Menor   | $2500
    2 |Adulto  | $5000
    3 |A.Mayor | $1000
    4 |Cerrar  |
    Dijite Opcion: ''')
menupreciod = ('''
Club de deportes "BUENA AVENTURA"

    N°|Entradas|Precio
    ------------------
    1 |Menor   | $2250
    2 |Adulto  | $4750
    3 |A.Mayor | $1000
    4 |Cerrar  |
    Dijite Opcion: ''')
menudia = ('''
Hoy es Viernes?
1)Si
2)No
Dijite Opcion: ''')
print("pedro...pedro..pedro..pe")
while True:
    try:
        b = int(input(menudia))
        if b == 2:
            while True:
                try:
                    a = int(input(menuprecio))
                    if a == 4:
                        break
                    elif a == 1:
                        cantem = int(input('Cuantas entradas quiere? :'))
                    if cantem == 0 :
                        input('COMPRA ANULADA') 
                    elif cantem >0:
                        print('Gracias por su compra')
                        cantem = 0+cantem
                    elif a == 2:
                        cantea = int(input('Cuantas entradas quiere? :'))
                    if cantea == 0 :
                        input('COMPRA ANULADA') 
                    elif cantea >0:
                        print('Gracias por su compra')
                        cantea = 0+cantea
                    elif a == 3:
                        canteam = int(input('Cuantas entradas quiere? :'))
                    if cantea == 0 :
                        input('COMPRA ANULADA') 
                    elif canteam >0:
                        print('Gracias por su compra')
                        canteam = 0+canteam
                    else:
                        input('ERORR DE RANGO')
                except ValueError:
                    continue
        if b == 1:
            input(f'HOY TENEMOS UN DESCUENTO ESPECIAL\nMenores 10% Descuento\nAdulto 5% Descuento')
        while True:
                try:
                    a = int(input(menupreciod))
                    if a == 4:
                        break
                    elif a == 1:
                        cantem = int(input('Cuantas entradas quiere? :'))
                    if cantem == 0 :
                        input('COMPRA ANULADA') 
                    elif cantem >0:
                        print('Gracias por su compra')
                        cantem = 0+cantem
                    elif a == 2:
                        cantea = int(input('Cuantas entradas quiere? :'))
                    if cantea == 0 :
                        input('COMPRA ANULADA') 
                    elif cantea >0:
                        print('Gracias por su compra')
                        cantea = 0+cantea
                    elif a == 3:
                        canteam = int(input('Cuantas entradas quiere? :'))
                    if cantem == 0 :
                        input('COMPRA ANULADA') 
                    elif canteam >0:
                        print('Gracias por su compra')
                        canteam = 0+canteam
                    else:
                        input('ERORR DE RANGO')
                except ValueError:
                    continue
                else:
                    input('ERROR DE RANGO  ')
                    continue
    except ValueError:
                continue
    while True:
            try:
                a = int(input(menupreciod))
                if a == 4:
                    break
                elif a == 1:
                    cantemD = int(input('Cuantas entradas quiere? :'))
                if cantemD == 0 :
                    input('COMPRA ANULADA') 
                elif cantemD >0:
                    print('Gracias por su compra')
                    cantemD = 0+cantemD
                elif a == 2:
                    canteaD = int(input('Cuantas entradas quiere? :'))
                if canteaD == 0 :
                    input('COMPRA ANULADA') 
                elif canteaD >0:
                    print('Gracias por su compra')
                    canteaD = 0+canteaD
                elif a == 3:
                    canteamD = int(input('Cuantas entradas quiere? :'))
                if cantemD == 0 :
                    input('COMPRA ANULADA') 
                elif canteamD >0:
                    print('Gracias por su compra')
                    canteamD = 0+canteamD
                else:
                    input('ERORR DE RANGO')
            except ValueError:
                continue
            print(f'entrada menores{cantem}\ncon descuento{cantemD}\entrada adultos{cantea}\ncon descuento{canteaD}\entrada Adulto Mayor{canteam}\ncon descuento{canteamD}')


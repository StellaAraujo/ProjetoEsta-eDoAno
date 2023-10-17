
print('\n\t\t\t  Estações do ano 2023 \n')

print('*Utilize o formato (dd/mm/aa)')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
print('\n')

# Processamento e saída
if mes == 1 or mes == 2 or mes == 3:
    if mes == 3 and dia >= 20:
        print('Estação: Outono')
    else:
        print('Estação: Verão')
elif mes == 4 or mes == 5 or mes == 6:
    if mes == 6 and dia >= 21:
        print('Estação: Inverno')
    else:
        print('Estação: Outono')
elif mes == 7 or mes == 8 or mes == 9:
    if mes == 9 and dia >= 23:
        print('Estação: Primavera')
    else:
        print('Estação: Inverno')
elif mes == 10 or mes == 11 or mes == 12:
    if mes == 12 and dia >= 22:
        print('Estação: Verão')
    else:
        print('Estação: Primavera')
else:
    print('Mês não identificado')







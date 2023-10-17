# Estações do ano 2023

print('\n\t\t\t Estações do Ano\n ')

print('*Utilize o formato (dd/mm/aa)')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))

print('\n')

if mes == 1 or mes == 2 or mes == 3:
    print('Estação: Verão')
elif mes == 4 or mes == 5 or mes == 6:
    print('Estação: Outono')
elif mes == 7 or mes == 8 or mes == 9:
    print('Estação: Inverno')
elif mes == 10 or mes == 11 or mes == 12:
    print('Estação: Primavera')
else:
    print('Mês não identificado')







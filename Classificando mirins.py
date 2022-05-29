from datetime import date
atual = date.today().year
nascimento = int(input('Ano do nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9 and 13:
    print('Classificação: MIRIM')
elif idade <= 14 and 18:
    print('Classificação: INFANTIL')
elif idade <= 19 and 24:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: MESTRE')
elif idade <= 39:
    print('Classificação: SUPREMO')


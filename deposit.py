per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float (input ("Введите сумму: "))
deposit = []
for key in per_cent:
    print (key, (per_cent[key]*money)/100)
    deposit.append ((per_cent[key]*money)/100)
print (deposit)
deposit.sort()
print("Размер наибольшего дохода:", deposit[-1])

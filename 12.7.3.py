per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))
perc = list(per_cent.values())

deposit = [round((i * money/100),2) for i in perc]

print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
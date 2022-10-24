# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
#
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
#
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
#
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.

Tickets = int(input("Введите кол-во билетов: "))
Ticket_price = 0
for i in range(Tickets):
    age = int(input("Возраст посетителя: "))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    elif age >= 25:
        price = 1390
    Ticket_price += price
if Tickets > 3:
    Ticket_price *= 0.9
print(f"Сумма к оплате: {int(Ticket_price)} руб.")
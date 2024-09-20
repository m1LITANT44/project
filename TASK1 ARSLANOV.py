from datetime import datetime, timedelta
now = datetime.today().date()
updated_time = now + timedelta(hours=1)
print("Доступные пиццы")
print("1: Маргарита")
print("2: Пепперони")
print("3: Грибная")
print("4: Четыре сыра")
print("5: Капричоза")
order = int(input("Какую пиццу вы хотите заказать? (Введите номер)"))
count = int(input("Сколько пицц вы хотите заказать? (Введите количество)"))
if order==1:
    rezult="Маргарита"

elif order==2:
    rezult="Пепперони"

elif order==3:
    rezult="Грибная"

elif order==4:
    rezult="Четыре сыра"

elif order==5:
    rezult="Карпичоза"

print(f"Вы заказали {count} пицц {rezult}")
quetion =(input("Готовы ли вы оставить отзыв? (да/нет)"))
if quetion=="нет":
    print("Спасибо, что воспользовались нашим сервисом!")
print(f"Заказ от {now} принят. Наш курьер подъедет к вам в течение часа (до {updated_time})")

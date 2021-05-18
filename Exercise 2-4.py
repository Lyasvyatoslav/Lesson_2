price_list = [29.98, 36.65, 7.8, 34.06, 43.09, 2.06, 12.56, 36.9, 34.8, 164]
for i in price_list:
    rub,\
    kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб. {int(kop):02d} коп.", end= ", ")

sort_prices = sorted(price_list)
ind = price_list.index
print("_" * 50)
for n in sort_prices:
     rub,\
     kop = str(f"{n:.2f}").split(".")
     print(f"{rub} руб. {int(kop):02d} коп.", end= ", ")
print("_" * 50, ind, price_list.index)

sort_prices = sorted(price_list, reverse = 1)
ind = price_list.index
print("_" * 50)
for n in sort_prices:
     rub,\
     kop = str(f"{n:.2f}").split(".")
     print(f"{rub} руб. {int(kop):02d} коп.", end= ", ")
print("_" * 50)
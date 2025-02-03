coffee = 1
milk = 2
visitors = 0
resept = {
    "type_coffee": ["coffee", "milk"],
    "espresso": [7, 0],
    "capuchino": [7, 100],
    "latte": [7, 180]
}

sklad = {
    "coffee": int,
    "milk": int
}

sklad["coffee"] = int(coffee * 1000)
sklad["milk"] = int(milk * 1000)

stop_capuchino = False
stop_latte = False


def run_coffee(type_coffee):
    global visitors, sklad, resept
    print(f"Варим {type_coffee} для посетителя №{visitors}")
    sklad["coffee"] = sklad["coffee"] - resept[type_coffee][0]
    sklad["milk"] = sklad["milk"] - resept[type_coffee][1]
    print(sklad)



while sklad["coffee"] > 7 and (stop_capuchino == False or stop_latte == False):
    if stop_capuchino == False and stop_latte == False:
        visitors += 1
        print(f"Пришел посетитель №{visitors}")
    else:
        break

    if visitors % 3 == 0 and visitors % 5 == 0:
        if sklad["milk"] >= 100:
            print(f"Посетитель №{visitors} заказал КАПУЧИНО.")
            run_coffee("capuchino")
        else:
            print(f"Посетитель №{visitors} заказал КАПУЧИНО.")
            print("НЕТ МОЛОКА, А НАДО!")
            stop_capuchino = True
            print(f"Посетителя №{visitors} обслужить нет возможности!")
            visitors -= 1
            break
    elif visitors % 3 == 0:
        if sklad["milk"] >= 100:
            print(f"Посетитель №{visitors} заказал КАПУЧИНО.")
            run_coffee("capuchino")
        else:
            print(f"Посетитель №{visitors} заказал КАПУЧИНО.")
            print("НЕТ МОЛОКА, А НАДО!")
            stop_capuchino = True
            print(f"Посетителя №{visitors} обслужить нет возможности!")
            visitors -= 1
            break
    elif visitors % 5 == 0:
        if sklad["milk"] >= 180:
            print(f"Посетитель №{visitors} заказал ЛАТТЕ.")
            run_coffee("latte")
        else:
            print(f"Посетитель №{visitors} заказал ЛАТТЕ.")
            print("НЕТ МОЛОКА, А НАДО!")
            stop_latte = True
            print(f"Посетителя №{visitors} обслужить нет возможности!")
            visitors -= 1
            break
    else:
        print(f"Посетитель №{visitors} заказал АМЕРИКАНО.")
        run_coffee("espresso")



print(f"ОБСЛУЖИЛИ {visitors} посетителей!")
from datetime import datetime
from os import system
from platform import platform


def get_num(msg: str, top_num: int = 24):
    while True:
        num = input(msg)
        try:
            num = int(num)
            if num < top_num:
                return num
            else:
                print(f"EL NUMERO NO PUEDE SER MAYOR A {top_num}")
        except ValueError:
            print("EL VALOR INGRESADO NO ES UN NUMERO!")


def get_next_day_or_this(my_hour: int):
    now = datetime.now()
    if now.replace(hour=my_hour) > now:
        return True
    else:
        return False


def get_hour(msg_create_time: str, msg_public_time: str):
    hour_to_create = None
    hour_to_public = None
    while True:
        system("cls" if "windows" in platform().lower() else "clear")
        now = datetime.now()
        print(f"+ HORA ACTUAL: {now.hour}")
        if not hour_to_create:
            hour_to_create = get_num(msg_create_time)
        if not hour_to_public:
            hour_to_public = get_num(msg_public_time)
        if hour_to_public <= hour_to_create:
            print(
                "LA HORA DE PUBLICACION NO PUEDE SER MENOR NI IGUAL QUE LA HORA DE CREACION!"
            )
            hour_to_public = None
            input("Enter para continuar... ")
        else:
            return hour_to_create, hour_to_public


if __name__ == "__main__":
    print(get_next_day_or_this(21))

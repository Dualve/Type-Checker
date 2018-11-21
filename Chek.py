def chekInput(message, type):
    try:
        if type == int:
            temp = int(input(message))
        elif type == float:
            temp = float(input(message))
        else:
            temp = str(input(message))
    except ValueError:
        print("Вы ввели неверное значение. Попробуйте еще раз!")
        return chekInput(message, type)
    return temp
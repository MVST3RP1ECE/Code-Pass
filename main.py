# Easy to remember Code/Pass generator

# Функция инициализации программы. Выбор категории код/пароль.
# Сначала реализую работы с категорией "Код". "Пароль" оставлю на потом :)
def chooseCatrgoryFunc():
    print(f"Выберите категорию:\n"
        f"1. Код\n"
        f"2. Пароль")
    chose = int(input("Введите цифру нужной категории:"))
    # print(chose)
    if chose == int(1):
        print("Вы выбрали категорию - Код ")
    elif chose == int(2):
        print("Вы выбрали категорию - Пароль ")
    else:
        print("Вы выбрали не существующую категорию!")
    return chose

numCategory = chooseCatrgoryFunc()
print(numCategory)


# Функция выбора длинны кода/пароля.
def choseLengthFunc(numCategory):
    if numCategory == int(1):
        print(f"Выберите длинну кода: \n"
              f"4. [4]\n"
              f"5. [5]\n"
              f"6. [6]")
        numLength = int(input("Введите цифру выбранной категории: "))
        if numLength == int(4):
            print("Длинна вашего кода будет - 4 цифры")
        elif numLength == int(5):
            print("Длинна вашего кода будет - 5 цифр")
        elif numLength == int(6):
            print("Длинна вашего кода будет - 6 цифр")
        else:
            print("Вы ввели некорректную длинну кода")

choseLengthFunc(numCategory)
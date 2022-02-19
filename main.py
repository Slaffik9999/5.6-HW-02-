field = [[" "," "," "],[" "," "," "],[" "," "," "]]#Пустое игровое поле
x = None
y = None

def greetings():
    #Распечатываем приветствие
    print("----------------------------------")
    print("Приветствуем вас в игре крестики-нолики")
    print("Первым начинает крестик, определитесь,")
    print("кто из вас будет играть крестиками")
    print("----------------------------------")

def print_field(field):
    #Распечатываем игровое поле
    print("----------------")
    print("   | 1 | 2 | 3 |")
    for i in range(len(field)):
        print("", i+1, "| ", end = "")
        for j in range(len(field[i])):
            print(field[i][j], end="")
            print(" | ", end = "")
        print()
    print("----------------")

def ask_coords():
    #Запрашиваем координаты
    cord = input("Введите координаты cтрока и столбец через пробел: ")
    #Проверка количества введённых значений
    if len(cord.split()) !=2:
        print("Введены неверные координаты")
        return -1, -1
    x, y = cord.split()[0], cord.split()[1]
    #Проверка являются ли цифрами
    if x.isdigit() and y.isdigit():
        x, y = int(x), int(y)
    else:
        print("Не введены числа")
        return -1, -1
    #Проверка на диапазон 1-3
    if x < 1 or x >3 or y < 1 or y >3:
        print("Координаты за пределами диапазона 1 - 3")
        return -1, -1
    return x, y

def check_cord(field, kr_nol):
    #Проверка координат на поле
    if field[c-1][d-1] != "X" and field[c-1][d-1] != "0":
        field[c-1][d-1] = kr_nol
        return field
    else:
        return False

def check_win(field):
    win_combinations = (((1,1),(2,2),(3,3)),
                        ((1,3),(2,2),(3,1)),
                        ((1,1),(1,2),(1,3)),
                        ((2,1),(2,2),(2,3)),
                        ((3,1),(3,2),(3,3)),
                        ((1,1),(2,1),(3,1)),
                        ((1,2),(2,2),(3,2)),
                        ((1,3),(2,3),(3,3))
                        )
    for comb in win_combinations:
        checklist = []
        for c in comb:
            checklist.append(field[c[0]-1][c[1]-1])
        if checklist == ["X", "X", "X"]:
            b = print_field(field)  # Выводим игровое поле
            print("Выиграл X!!!")
            return True
        if checklist == ["0", "0", "0"]:
            b = print_field(field)  # Выводим игровое поле
            print("Выиграл 0!!!")
            return True
    return False

#Начало
a = greetings()#Выводим комментарии на начало игры

for steps in range(9):
    #Задаём Х или 0 в зависимости от чётности шагов
    if steps %2 == 0:
        kr_nol = "X"
    else:
        kr_nol = "0"

    b = print_field(field)#Выводим игровое поле

    while True:
        c, d = ask_coords()#Запрашиваем координаты у игрока
        if c+d != -2:
            break
    e = check_cord(field, kr_nol)#Проверяем клетку поля на занятость
    f = check_win(field)#Проверяем поле на выигрыш Х или 0
    if f == True:#Если выигрыш уже состоялся, то выход из цикла
        break
    if steps == 8:#Если никто не выиграл
        b = print_field(field)  # Выводим игровое поле
        print("Ничья")
print("Спасибо за игру")

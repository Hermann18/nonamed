import time
print("начало.работы")

route_actual = open("route", "r").read().split(";")
# settings = open("computerInput", "+")
# sett = settings.read()
# computerOutput = open("computerOutput", "+")
# dataBase = open("dataBase", "w")

coordinatesActual = 0

stillWorking = True

def findValue(what):
    settings = open("computerInput", "r").read()

    n = settings[ settings.find(what) + len(what) + 2: ]
    # print( n[:n.find(";")], f"-{what}")
    return n[:n.find(";")]


print("\n _________________________")

auto = eval(findValue("auto"))
connectedEthernet = eval(findValue("connectedEthernet"))    
coordinatesMax = int(findValue("coordinatesMax"))           #Максимальная длина выезда
normalDiameter =int(findValue("normalDiameter"))          #нормальный диаметр, получаем из приложения
normalDelta =  int(findValue("normalDelta"))             #нормальное отклонение диаметра, задаем в приложении
print(auto, connectedEthernet, coordinatesMax, normalDiameter, normalDelta)

issues = []

# print( open("computerInput", "r").read())

def diamat(connectedEthernet, step): # функция анализа окружающей среды
    issues_new = []

    degrees_result = []
    for i in range (0, 72):
        degrees_result.append(int (route_actual[coordinatesActual].split(",")[i*5]) ) #Получаем данные с лазерной ерунды
    for i in range (0, 36):
        if normalDiameter - (degrees_result[i] + degrees_result[i + 36]) > normalDelta:
            issues_new.append( [coordinatesActual, "0"] ) #Записываем проблемы
    
    # print("работаем Ультразвуковой ЭМА-контроль")
    # print("Получаем некоторые данные. Если они инвалиды - записываем в массив issues_new массив [a,z] где а - координаты и z - код проблемы")

    # print("работаем Метод динамического скин-слоя")
    # print("Получаем некоторые данные. Если они инвалиды - записываем в массив issues_new массив [a,z] где а - координаты и z - код проблемы")

    for i in issues_new:
        issues.append(i) #Либо сохраняем как бек-ап, либо как единственный источник информации
        k = open("dataBase", "r").read()
        k = k + f"{i},"
        # print(k)
        open("dataBase", "w").write( k )
        if connectedEthernet == True:  
            k = open("computerOutput", "r").read() 
            k = k + f"{i},"
            # print(k)
            open("computerOutput", "w").write( k ) #Передаем данные на компьютеры
    

def findOurDegrees(degree, step_route):
    return step_route.split(",")[degree]

def back():
    global coordinatesActual
    while coordinatesActual != 0:
        coordinatesActual -= 1
        time.sleep(1)

while (stillWorking):
    print(coordinatesActual);
    #  time.sleep(1)
    if connectedEthernet == True:
        auto = eval( findValue("auto") ) 
    if (auto):
        if coordinatesActual < coordinatesMax:
            coordinatesActual += 1 #проверяем, можно ли делать шаг, делаем.шаг
        else:  #если нет - возвращаемся обратно (ездой назад)
            back()
        diamat(connectedEthernet, coordinatesActual)
    else:
        btt_block = False #снимаем блок на нажатие кнопок. Тк очеивдно что выполнение кода занимает время и поэтому нельзя всегда рарзрешать жать на кнопки
        while (True):
            time.sleep(1)
            if eval(findValue("diamat")) == True:
                diamat(connectedEthernet, coordinatesActual)
                k = 0
                k = open("computerInput", "r").read()
                k = k.replace("diamat =True;", "diamat =False;")
                # print(k)
                open("computerInput", "w").write(k)
            if connectedEthernet != eval(findValue("connectedEthernet")):
                connectedEthernet = eval(findValue("connectedEthernet"))
                break
            if auto != eval(findValue("auto")):
                auto = eval(findValue("auto"))
                break
            if int(findValue("forward")) != 0:
                coordinatesActual += int(findValue("forward"))
                val = int(findValue("forward"))
                k = open("computerInput", "r").read()
                k = k.replace(f"forward ={val};", "forward =0;")
                # print(k)
                open("computerInput", "w").write(k)
            
            

        # print("провереям нажатие кнопки авто, включаем авто режим, если кнопка была нажата")
        # print("провереям нажатие кнопки вперед/назад, едим, если кнопка была нажата и хватает длины")
        # print("провереям новые данные с жойстика, вращаем если можно")
        # print("делаем все через отдельные функции, ждем пока что-нибудь нажмут. Нажимают - блокируем кнопки и начинаем новую итерацию цикла while")

print("путь закончен");


# Отдельным потоком делаем передачу видео. Не знаю как оформить
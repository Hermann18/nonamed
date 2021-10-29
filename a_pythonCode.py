import time
print("начало.работы")

route_actual = open("route", "r").read().split(";") #Из этого файла получаем данные как будто от датчиков
#selfDataBase - файл с данными которые сохраняются на самом устройстве 
#outputToComputer - что передается на компьютер 
#inputFromComputer - данные которые приходят нашему устройство, в основном настройки 

coordinatesActual = 0   #переменная отвечает за координаты в у.е. 

stillWorking = True     #ну очевидно

def findValue(what):    #для поиска определенных значений из файла с "настрйками"
    settings = open("inputFromComputer", "r").read()

    n = settings[ settings.find(what) + len(what) + 2: ]
    # print( n[:n.find(";")], f"-{what}")
    return n[:n.find(";")]  

print("\n_____________")

auto = eval(findValue("auto"))  #переменная отвечающая за режим "авто"
connectedEthernet = eval(findValue("connectedEthernet"))    #переменная отвечающая за включение etherneta
coordinatesMax = int(findValue("coordinatesMax"))           #максимальная длина выезда
normalRadius =int(findValue("normalRadius"))          #нормальный радиус, получаем из приложения ( поскольку приложения нет - из файла)
normalDelta =  int(findValue("normalDelta"))             #нормальное отклонение радиуса, задаем в приложении ( поскольку приложения нет - в файле)
print(auto, connectedEthernet, coordinatesMax, normalRadius, normalDelta)     #проверяем

issues = [] #проблемки

def diamat(): # функция анализа окружающей среды
    global connectedEthernet, coordinatesActual
    issues_new = []

    degrees_result = []
    for i in range (0, 72):     
        if normalRadius - int(route_actual[coordinatesActual].split(",")[i*5]) > normalDelta:
            issues_new.append( [coordinatesActual, "0", i*5] ) #Если проблема - записываем, с кодом, координатой и градусамиы
    
    # print("работаем Ультразвуковой ЭМА-контроль") 
    # print("Получаем некоторые данные. Если они инвалиды - записываем в массив issues_new массив [a,z] где а - координаты и z - код проблемы")

    # print("работаем Метод динамического скин-слоя") По-сути код аналогичен вышенаписанному 
    # print("Получаем некоторые данные. Если они инвалиды - записываем в массив issues_new массив [a,z] где а - координаты и z - код проблемы")

    for i in issues_new: #Обновляем файлики с проблемками записанными на самом устройстве и "отправляем их на пк", если есть родключение  
        issues.append(i) 
        k = open("selfDataBase", "r").read() + f"{i},"
        open("selfDataBase", "w").write( k )
        if connectedEthernet == True:  
            k = open("outputToComputer", "r").read() + f"{i},"
            open("outputToComputer", "w").write( k ) #Передаем данные на компьютеры
    

def findOurDegrees(degree, step_route):     #Как бы получам данные с лазерной шляпы
    return step_route.split(",")[degree]

def back():
    global coordinatesActual
    while coordinatesActual > 0:
        doStep(-1)
        time.sleep(1)

def doStep(vector):
    global coordinatesActual
    print(vector)
    if coordinatesActual + (vector * 1) <= coordinatesMax and coordinatesActual + (vector * 1) >= 0:
        coordinatesActual = coordinatesActual + (vector * 1)

while (stillWorking):
    print(coordinatesActual) 
    if connectedEthernet == True:
        auto = eval( findValue("auto") ) 
    if (auto):
        if coordinatesActual < coordinatesMax:
            doStep(1)   #проверяем, можно ли делать шаг, делаем.шаг
        else:  #если нет - возвращаемся обратно (ездой назад)
            back()
        diamat()
    else:
        btt_block = False #снимаем блок на нажатие кнопок. Тк очеивдно что выполнение кода занимает время и поэтому нельзя всегда рарзрешать жать на кнопки
        while (True):
            time.sleep(0.5)
            if eval(findValue("diamat")) == True:
                diamat()
                k = open("inputFromComputer", "r").read()
                k = k.replace("diamat =True;", "diamat =False;")
                open("inputFromComputer", "w").write(k)
            if connectedEthernet != eval(findValue("connectedEthernet")):
                connectedEthernet = eval(findValue("connectedEthernet"))
                break
            if auto != eval(findValue("auto")):
                auto = eval(findValue("auto"))
                break
            if int(findValue("forward")) != 0:
                vector = 1
                val = int(findValue("forward"))
                print(val)
                if val < 0:
                    vector = -1
                    val = val * -1
                for i in range(val):
                    doStep(vector)
                val = int(findValue("forward"))
                k = open("inputFromComputer", "r").read()
                k = k.replace(f"forward ={val};", "forward =0;")
                #print(k)
                open("inputFromComputer", "w").write(k)
                break
            
print("путь закончен");


# Отдельным потоком делаем передачу видео. Не знаю как оформить
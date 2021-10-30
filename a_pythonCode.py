print("начало.работы")

coordinatesActual = 0   #переменная отвечает за координаты в у.е. 

stillWorking = True     #ну очевидно

def findValue(what):    #для поиска определенных значений из файла с "настрйками"
    settings = open("inputFromComputer", "r").read()

    n = settings[ settings.find(what) + len(what) + 2: ]
    # print( n[:n.find(";")], f"-{what}")
    return n[:n.find(";")]  

print("\n_____________")

open("selfDataBase", "w").write("")
open("outputToComputer", "w").write("")

route_actual = open("route", "r").read().split(";")         #маршрут
coordinatesMax = int(findValue("coordinatesMax"))           #максимальная длина выезда
normalRadius =int(findValue("normalRadius"))                #нормальный радиус, получаем из приложения ( поскольку приложения нет - из файла)
normalDelta = int(findValue("normalDelta"))                #нормальное отклонение радиуса, задаем в приложении ( поскольку приложения нет - в файле)
lidarsCoordinates = [0, 90, 180, 270]                       #где Лидары
print(coordinatesMax, normalRadius, normalDelta)            #проверяем

issues = [] #проблемки

def diamat(): # функция анализа окружающей среды
    global coordinatesActual
    issues_new = []

    degrees_result = []
    for i in range(360):
        degrees_result.append("x")
    for i in range(len(lidarsCoordinates)):
        for x in range(45):
            lidarsCoordinates[i] = (lidarsCoordinates[i] + 1) % 360
            degrees_result[lidarsCoordinates[i]] = int(route_actual[coordinatesActual].split(",")[lidarsCoordinates[i]])

    for u in range(len(degrees_result)):
        if degrees_result[u] != "x" and normalRadius - degrees_result[u] > normalDelta:
            issues_new.append([coordinatesActual, u])

    for i in issues_new: #Обновляем файлики с проблемками записанными на самом устройстве
        issues.append(i) 
        k = open("selfDataBase", "r").read() + f"{i},"
        open("selfDataBase", "w").write( k )
    
    k = open("outputToComputer", "r").read() + f"{degrees_result}; \n"
    open("outputToComputer", "w").write(k)

def lazer(): #симуляция возможности приграды которую не проехать
    if randint.random(0,100) < 10:
        return False 

def back():
    global coordinatesActual
    while coordinatesActual > 0:
        doStep(-1)
        #print(coordinatesActual)

def doStep(vector):
    global coordinatesActual
    if coordinatesActual + (vector * 1) <= coordinatesMax and coordinatesActual + (vector * 1) >= 0:
        coordinatesActual = coordinatesActual + (vector * 1)

while (stillWorking):
    #print(coordinatesActual) 
    if coordinatesActual < coordinatesMax and lazer():
        doStep(1)   #проверяем, можно ли делать шаг, делаем.шаг
        diamat()
    else:  #если нет - возвращаемся обратно (ездой назад)
        back()
        stillWorking = False
   
            
print("путь закончен");


# Отдельным потоком делаем передачу видео. Не знаю как оформить

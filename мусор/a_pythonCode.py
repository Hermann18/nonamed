import time
print("начало.работы")


coordinatesActual = 0   #переменная отвечает за координаты в у.е. 

stillWorking = True     #ну очевидно

def findValue(what):    #для поиска определенных значений из файла с "настрйками"
    settings = open("inputFromComputer", "r").read()

    n = settings[ settings.find(what) + len(what) + 2: ]
    # print( n[:n.find(";")], f"-{what}")
    return n[:n.find(";")]  

print("\n_____________")

route_actual = open("route", "r").read().split(";")
coordinatesMax = int(findValue("coordinatesMax"))           #максимальная длина выезда
normalRadius =int(findValue("normalRadius"))          #нормальный радиус, получаем из приложения ( поскольку приложения нет - из файла)
normalDelta =  int(findValue("normalDelta"))             #нормальное отклонение радиуса, задаем в приложении ( поскольку приложения нет - в файле)
coord_lidar = [0, 90, 180, 270]
print(coordinatesMax, normalRadius, normalDelta)     #проверяем

issues = [] #проблемки

def diamat(): # функция анализа окружающей среды
    global coordinatesActual
    issues_new = []

    degrees_result = []
    for i in range(360):
        degrees_result.append("x")
    for i in coord_lidar:     
        for x in range(1, 43):
            degrees_result[i+x] = int(route_actual[coordinatesActual].split(",")[i + x])
            degrees_result[i-x] = int(route_actual[coordinatesActual].split(",")[i - x])
        for u in range(len(degrees_result)):
            if normalRadius - degrees_result[u] > normalDelta:
                issues_new.append(coordinates_actual, u)

    for i in issues_new: #Обновляем файлики с проблемками записанными на самом устройстве
        issues.append(i) 
        k = open("selfDataBase", "r").read() + f"{i},"
        open("selfDataBase", "w").write( k )
    k = open("outputToComputer", "r").read() + degrees_result
    open("outputToComputer", "w").write( k )

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
    for i in coord_lidar:
        i = (i + 45)%360

while (stillWorking):
    print(coordinatesActual) 
    if coordinatesActual < coordinatesMax:
        doStep(1)   #проверяем, можно ли делать шаг, делаем.шаг
        diamat()
    else:  #если нет - возвращаемся обратно (ездой назад)
        back()
   
            
print("путь закончен");


# Отдельным потоком делаем передачу видео. Не знаю как оформить
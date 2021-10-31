print("начало работы")
from random import randint
import threading

video = 1

f = open("route", "w")
coordinatesActual = 0   #переменная отвечает за координаты в у.е. 
EMA_Degrees = [0,120,240]
powers = [1,1,1]


def diamat():
    degrees = []
    for y in range(360):
        degrees.append("x")
    for i in range(len(EMA_Degrees)):
        for x in range(120):
            EMA_Degrees[i] = (EMA_Degrees[i] + 1) % 360
            degrees[EMA_Degrees[i]] = randint(3,6)
    gyroscope = [randint(0, 359), randint(0, 359), randint(0, 359)]
    sr = f":{degrees}=\n={gyroscope}; \n"
    f = open("route", "r").read();
    open("route", "w").write(f"{f}{sr}")

def first_thread():
    global coordinatesActual, video
    print("ситстемы в норме")
    while True:
        diamat()
        lazers = [randint(0,100),randint(0,100,),randint(0,100,)]
        if lazers[0] < 20 and lazers[1] < 20 and lazers[2] < 20:
            print("vse")
            video = 0
            break
        if lazers[0] != lazers[1] or lazers[1] != lazers[2] or lazers[0] != lazers[2]:
            for i in range(len(lazers)):
                if lazers[i] == max(lazers):
                    powers[i] = 0.2
                else:
                    powers[i] = 1
        coordinatesActual += 1

def second_thread():
    global video
    while video:
      print("запись видео") 
first = threading.Thread(target = first_thread, name = "a")
second = threading.Thread(target = second_thread, name = "c")
first.start()
second.start()


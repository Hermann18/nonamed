Первый поток:
    Включить прожектор
    Проверить роботоспособность всех систем
    Повторяй пока "Истина":
        Повторяй 120 раз:
            Опроси датчик ЭМА_1
            Сохрани результат
            Опроси датчик ЭМА_2
            Сохрани результат
            Опроси Датчик ЭМА_3
            Сохрани результат 
            Повернись по сечению трубы против часовой стрелки на градус 
        Опроси гироскоп
        Сохрани результат
        Проверка трех датчиков расстояния
        Если на всех расстояния менее 20 см:
            все колеса СТОП
        Если расстояние на датчиках различается:
            Находим колесо с большим расстоянием
            Включаем пониженную скорость этому колесу   
        Если расстояние на датчиках одинаково:
            Включаем всем колесам нормальную скорость
        Колеса продвигаются вперед согласно своей скорости
    Завершить запись видео

Второй поток:
    Запись видео

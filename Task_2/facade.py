import random

from russian_names import RussianNames

SPEED = (0, 5, 7, 8, 21, 26, 30, 33, 36, 40)
FORSE = (50, 0, 66, 79, 100)


class _Wind(object):
    """
    Класс ветра.
    """

    def __init__(self, speed=0):
        # Скорость ветра
        self._speed = speed

        @property
        def speed(self):
            return self._speed

        @speed.setter
        def level(self, speed):
            self._speed = speed


class _Rain(object):

    """
    Класс дождя.
    """

    def __init__(self, forse=0):
        pass
        # сила дождя
        self.forse = forse


class _NotificationSystem(object):
    """
    Класс системы оповещения
    """
    def __str__(self):
        return 'Система оповещения'

    def status_check(self):
        print(f'\n{self} была включена и спасла много людей')


# Facade
class Hurricane(object):

    def __init__(self):
        self.name = RussianNames(
            count=1, surname=False, patronymic=False
        ).get_batch()[0]
        self.energy = _Wind()
        self.component = _Rain()
        self.need = _NotificationSystem()
        self.component.forse = random.choice(FORSE)
        self.energy._speed = random.choice(SPEED)

    def start(self):
        print('\nБыло объявлено предупреждение...')
        if self.energy._speed < 10 and self.component.forse < 77:
            print('\n но осталась тихая погода')

    def drive(self):

        print('\n')

        if self.energy._speed >= 33:

            while self.energy._speed >= 0 and self.component.forse > 0:

                print(f'Ураган по имени {self.name} двигается в сторону города')
                print(f'Но сила ветра начинает стихать {self.energy._speed} м/с')

                self.energy._speed -= 10.5
                self.component.forse -= 5

            self.stop()
            self.need.status_check()

        elif 21 < self.energy._speed < 33:

            print(f'На город обрушился шторм скоростью {self.energy._speed} м/с')

            self.need.status_check()

        elif 11 <= self.energy._speed <= 21:

            print(f'В городе был шквалистый ветер скоростью {self.energy._speed} м/с')

        elif self.energy._speed == 0:

            print(f'Полный штиль')

        else:
            print(f'Был легкий и свежий бриз')

    def stop(self):
        print('\nВсё стихло')


def main():
    hurricane = Hurricane()
    hurricane.start()
    hurricane.drive()


if __name__ == '__main__':
    main()

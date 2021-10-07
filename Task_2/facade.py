from russian_names import RussianNames


class _Wind(object):
    """
    Класс ветра.
    """

    def __init__(self, speed=70):
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

    def __init__(self, forse=100):
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

    def start(self):
        print('\nБыло объявлено предупреждение...')

    def drive(self):
        print('\n')
        if self.energy._speed != 0:
            while self.energy._speed >= 0 and self.component.forse > 0:
                print(f'Ураган по имени {self.name} двигается в сторону города')
                print(f'Сила ветра начинает стихать {self.energy._speed}')
                self.energy._speed -= 10.5
                self.component.forse -= 5

    def stop(self):
        print('\nВсё стихло')

    def notification(self):
        self.need.status_check()


def main():
    hurricane = Hurricane()
    hurricane.start()
    hurricane.drive()
    hurricane.stop()
    hurricane.notification()


if __name__ == '__main__':
    main()

class Monogamous:
    """Класс одиночки"""
    __instance__ = None

    def __init__(self):
        """ Конструктор"""
        if Monogamous.__instance__ is None:
            Monogamous.__instance__ = self
        else:
            raise Exception('Таких больше нет')

    @staticmethod
    def get_instance():
        """Получение экземпляра класса"""
        if not Monogamous.__instance__:
            Monogamous()
        return Monogamous.__instance__


def main():
    monogamous = Monogamous()
    print(monogamous)

    same_monogamous = Monogamous.get_instance()
    print(same_monogamous)

    another_monogamous = Monogamous.get_instance()
    print(another_monogamous)

    new_monogamous = Monogamous()
    print(new_monogamous)


if __name__ == '__main__':
    main()

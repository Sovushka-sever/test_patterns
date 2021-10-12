class EmployeeAlertSystem:
    """Класс сотрудника."""

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'Сотрудник {self.name}, {message}')


class VisitorAlertSystem:
    """Класс посетителя."""
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f'Посетитель {self.name}, {message}')


class NotificationSystem:
    """Класс системы оповещения."""

    def __init__(self):
        self.subscribers = dict()

    def connection(self, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def shutdown(self, who):

        print(f'Вы отключили систему оповещения')
        del self.subscribers[who]

    def notify(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)


def main():
    system = NotificationSystem()
    visitor_rita = VisitorAlertSystem('Рита')
    employee_alla = EmployeeAlertSystem('Алла')
    employee_oleg = EmployeeAlertSystem('Олег')

    system.connection(visitor_rita, visitor_rita.receive)
    system.connection(employee_alla, employee_alla.update)
    system.connection(employee_oleg)

    system.notify('требуется ваше участие')
    system.shutdown(employee_oleg)
    system.notify('подходите по мере возможности')

    message = input('Введите своё сообщение ')
    system.notify(f'{message}')


if __name__ == '__main__':
    main()


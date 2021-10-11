import random


class SadMood:
    """Класс грустных мыслей"""

    def __init__(self):
        self.new_emotion = {
            'действие': 'злость',
            'эмоция': 'тоска',
            'противодействие': 'смех'
        }

    def reaction(self, msg):

        if msg == 'действие':
            result = f'Грустное настроение вызывает {self.new_emotion.get(msg, msg)}'
        elif msg == 'эмоция':
            result = f'Подпитывает грустное настроение {self.new_emotion.get(msg, msg)}'
        elif msg == 'противодействие':
            result = f'Лучшее лекарство {self.new_emotion.get(msg, msg)}'

        return result


class NormalMood:
    """Класс нормального настроения"""

    def __init__(self):
        self.new_emotion = {
            'действие': 'спокойным',
            'эмоция': 'равновесие',
            'противодействие': 'улыбка'}

    def reaction(self, msg):

        if msg == 'действие':
            result = f'Нормальное настроение бывает {self.new_emotion.get(msg, msg)}'
        elif msg == 'эмоция':
            result = f'Заряжает настроение {self.new_emotion.get(msg, msg)}'
        elif msg == 'противодействие':
            result = f'Иногда застает {self.new_emotion.get(msg, msg)}'

        return result


class PositiveMood:
    """Класс позитивных мыслей"""

    def __init__(self):
        self.new_emotion = {
            'действие': 'смех',
            'эмоция': 'радость',
            'противодействие': 'грусть'}

    def reaction(self, msg):

        if msg == 'действие':
            result = f'Хорошее настроение вызывает {self.new_emotion.get(msg, msg)}'
        elif msg == 'эмоция':
            result = f'Заряжает позитив {self.new_emotion.get(msg, msg)}'
        elif msg == 'противодействие':
            result = f'Иногда застает {self.new_emotion.get(msg, msg)}'

        return result


def Factory(mood=None):
    """Фабрика настроения"""

    moods = {
        'Sad': SadMood,
        'Normal': NormalMood,
        'Positive': PositiveMood,
    }

    return moods[mood]()


if __name__ == "__main__":

    attitude_sad = Factory('Sad')
    attitude_norm = Factory('Normal')
    attitude_positive = Factory('Positive')

    actions = ['действие', 'эмоция', 'противодействие']
    action = random.choice(actions)

    print(attitude_sad.reaction(action))
    print(attitude_norm.reaction(action))
    print(attitude_positive.reaction(action))
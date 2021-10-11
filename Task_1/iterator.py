class Films:
    """Класс для перебора фильмов."""
    def __init__(self):
        self.films_list = [
            'Неоновый демон',
            'Валериан и город тысячи планет',
            'Мой парень псих',
            'Дело храбрых',
            'В центре внимания',
            'Зверополис',
            'Субурбикон',
            'Иностранец',
            'Коматозники',
            'Глубоководный горизонт',
            'Манчестер у моря',
            'Голос монстра',
            'Прибытие',
            'Скрытые фигуры',
          ]

    def __len__(self):
        return len(self.films_list)

    def __iter__(self):
        return self.FilmsIterator(self)

    class FilmsIterator:
        """Итератор для фильмов."""
        def __init__(self, films):
            self.__films = films
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            film_list = self.__films.films_list[self.__index]
            self.__index += 1

            if self.__index >= len(self.__films):
                raise StopIteration('На сегодня подборка фильмов закончена')

            return film_list


def main():
    films = Films()

    for color in films:
        print(color)


if __name__ == '__main__':
    main()

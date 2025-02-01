import doctest


class Car:
    """
    Абстрактный класс для описания мебели.
    """

    def __init__(self, color: str, weight: int, x: int = 0, y: int = 0, fuel: int = 0):
        """
        :param color: Цвет автомобиля.
        :param weight: Вес автомобиля в килограммах. Должен быть положительным.
        :param x, y: Координаты автомобиля.
        :param fuel: Наличие топлива в автомобиле.

        Примеры:
        >>> car = Car('Blue', 1500, 0, 0, 0)
        """

        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть типа str.")

        if not isinstance(weight, int):
            raise TypeError("Вес автомобиля должен быть типа int.")

        if not isinstance(x, int):
            raise TypeError("Координата x автомобиля должна быть типа int.")

        if not isinstance(y, int):
            raise TypeError("Координата y автомобиля должна быть типа int.")

        if weight <= 0:
            raise ValueError("Вес автомобиля должен быть положительным.")

        if len(color) == 0:
            raise ValueError("У автомобиля должен быть цвет.")

        self.color = color
        self.weight = weight
        self.x = x
        self.y = y

    def drive(self, x: int, y: int) -> None:
        """
        Управление автомобилем.

        :return: Изменение положения автомобиля.

        >>> car = Car("Blue", 1500, 0, 0, 0)
        >>> car.drive(10, 0)
        """

    def fuel(self) -> bool:
        """
        Проверка есть ли топливо в автомобиле.

        :return: Наличие топлива в автомобиле.

        Примеры:
        >>> car = Car("Blue", 1500, 0, 0, 0)
        >>> car.fuel()
        """


class Tree:
    """
    Абстрактный класс для описания дерева.
    """

    def __init__(self, species: str, age: int, dead: bool = False):
        """
        :param species: Вид дерева.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.

        Примеры:
        >>> tree = Tree('deciduous', 20)
        """

        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str.")

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int.")

        if len(species) == 0:
            raise ValueError("Укажите вид дерева.")

        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.age = age

    def is_dead(self) -> bool:
        """
        Живое ли дерево.

        :return: Проверка живое дерево или нет.

        >>> tree = Tree('deciduous', 20)
        >>> tree.is_dead()
        """

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева.

        :param years: Количество лет, на которое увеличивается возраст. Должно быть положительным.

        :return: Возраст дерева

        >>> tree = Tree('deciduous', 20)
        >>> tree.grow(200)
        """
        if years <= 0:
            raise ValueError("Годы роста должны быть положительными.")
        self.age += years


class Library:
    """
    Абстрактный класс для описания Библиотеки>.
    """

    def __init__(self, address: str, active_readers: int):
        """
        :param address: Адрес библиотеки.
        :param active_readers: Количество активных читателей. Должно быть неотрицательным.
        Примеры:
        >>> library = Library("Москва", 1001)
        """
        if not isinstance(address, str):
            raise TypeError("Адрес библиотеки должен быть типа str")

        if active_readers < 0:
            raise ValueError("Количество активных читателей не может быть отрицательным.")

        self.address = address
        self.active_readers = active_readers

    def register(self, registered_readers: int = 1) -> None:
        """
        Функция, которая регистрирует нового читателя.

        :param registered_readers: Информация о читателе.

        :return: Сохраняет новое количество читателе.

        >>> library = Library("Москва", 1001)
        >>> library.register()
        """

    def remove(self, remove_reader: int = 1) -> None:
        """
        Функция, которая удаляет читателя.

        :return: Новое количество читателей после удаления.

       >>> library = Library("Москва", 1001)
       >>> library.remove()
        """
        if self.active_readers <= 0:
            raise ValueError("Количество читателя должен быть положительным.")
        self.active_readers -= remove_reader


if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации

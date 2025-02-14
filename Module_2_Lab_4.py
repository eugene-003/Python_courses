class Car:
    """Базовый класс автомобиля

    :param color: Цвет автомобиля.
    :param weight: Вес автомобиля в килограммах. Должен быть положительным.
    :param _number: Номер на автомобиле.
    :param x, y: Координаты автомобиля.

    Примеры:
        >>> car = Car('Blue', 1500, 4274319, 0, 0, 0)
    """

    def __init__(self, color: str, weight: int, _number: int, x: int = 0, y: int = 0, fuel: int = 0):
        self.color = color
        self.weight = weight
        self.number = _number
        self.x = x
        self.y = y
        self.fuel = fuel

    def fuel(self):
        """Заправка автомобиля топливом.

                :return: None
                """
        print(f"Заправляем автомобиль {self.number} топливом.")

    def __str__(self) -> str:
        return f"Машина {self.number} {self.color} цвета с массой {self.weight} тонн."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(numder={self.number!r}, color={self.color!r}, weight={self.weight})"


class PassengerCar(Car):
    """Дочерний класс легкового автомобиля.

        :param number_of_passengers: Количество пассажиров в автомобиле.
        Примеры:
            >>> passenger_car = PassengerCar('Red', 1200, 123456, number_of_passengers=4)
        """

    def __init__(self, color: str, weight: int, number: int, x: int = 0, y: int = 0, fuel: int = 0,
                 number_of_passengers: int = 1):
        super().__init__(color, weight, number, x, y, fuel)
        self.number_of_passengers = number_of_passengers

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(numder={self.number!r}, color={self.color!r}, weight={self.weight}, number_of_passengers={self.number_of_passengers})"

    def fuel(self):
        """Заправка легкового автомобиля бензином.

                :return: None
                """
        print(f"Заправляем легковой автомобиль {self.number} бензином.")


class CargoTruck(Car):
    """Дочерний класс грузового автомобиля.

      :param load_capacity: Грузоподъемность автомобиля.
      Примеры:
          >>> cargo_truck = CargoTruck('Blue', 5000, 654321, load_capacity=1000)
      """

    def __init__(self, color: str, weight: int, number: int, x: int = 0, y: int = 0, fuel: int = 0,
                 load_capacity: int = 1):
        super().__init__(color, weight, number, x, y, fuel)
        self.load_capacity = load_capacity

    def fuel(self):
        """Заправка легкового автомобиля бензином.

                :return: None
                """
        print(f"Заправляем грузовой автомобиль {self.number} дизельным топливом.")

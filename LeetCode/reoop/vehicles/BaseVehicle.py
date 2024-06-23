from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    MAX_BATTERY = 100

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip() == '':
            raise ValueError('Brand cannot be empty!')

        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip == '':
            raise ValueError('Model cannot be empty!')

        self.__model = value

    @property
    def driving_license_number(self):
        return self.__license_plate_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if value.strip == '':
            raise ValueError('License plate number is required!')

        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = self.MAX_BATTERY

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {'OK' if self.is_damaged is False else 'Damaged'}"

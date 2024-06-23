from BaseVehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = int(mileage / self.MAX_MILEAGE * 100) + 5
        self.battery_level -= percentage

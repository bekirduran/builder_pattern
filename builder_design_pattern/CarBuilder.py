from builder_design_pattern.Car import Car
from builder_design_pattern.ICarBuilder import ICarBuilder


class CarBuilder(ICarBuilder):

    def __init__(self):
        self.car = Car()

    def set_car_brand(self, brand):
        self.car.brand = brand
        return self

    def set_car_model(self, model):
        self.car.model = model
        return self

    def set_number_doors(self, door):
        self.car.door = door
        return self

    def set_sunroof(self, bool):
        self.car.sunroof = bool
        return self

    def set_engine_size(self, size):
        self.car.engine_size = size
        return self

    def set_max_speed(self, speed):
        self.car.max_speed = speed
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_armor(self, armor):
        self.car.armor = armor
        return self

    def set_hybrid(self, bool):
        self.car.hybrid = bool
        return self

    def set_turbo(self, bool):
        self.car.turbo = bool
        return self

    def set_black_box(self, bool):
        self.car.black_box = bool
        return self

    def get_result(self):
        return self.car

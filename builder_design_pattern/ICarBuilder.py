from abc import ABCMeta, abstractmethod


class ICarBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_car_brand(brand):
        "Build type"

    @staticmethod
    @abstractmethod
    def set_car_model(model):
        "Build material"

    @staticmethod
    @abstractmethod
    def set_number_doors(door):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_sunroof(bool):
        "Has sunroof or not"

    @staticmethod
    @abstractmethod
    def set_engine_size(size):
        "Size of Engine"

    @staticmethod
    @abstractmethod
    def set_max_speed(speed):
        "max speed"

    @staticmethod
    @abstractmethod
    def set_color(color):
        "Car color"

    @staticmethod
    @abstractmethod
    def set_armor(armor):
        "Has armor or not"

    @staticmethod
    @abstractmethod
    def set_hybrid(bool):
        "Hybrid car or not"

    @staticmethod
    @abstractmethod
    def set_turbo(bool):
        "Has car turbo"

    @staticmethod
    @abstractmethod
    def set_black_box(bool):
        "Has car blackbox or not"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"


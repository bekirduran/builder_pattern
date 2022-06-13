
from builder_design_pattern.CarBuilder import CarBuilder


class AudiCarBuilder:

    @staticmethod
    def construct():
        return CarBuilder() \
            .set_car_brand("Audi") \
            .set_car_model("A5") \
            .set_number_doors(2) \
            .set_sunroof(True) \
            .set_color("White") \
            .set_armor(True) \
            .set_turbo(True) \
            .set_max_speed(420) \
            .get_result()

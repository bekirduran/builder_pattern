
from builder_design_pattern.CarBuilder import CarBuilder


class BMWCarBuilder:

    @staticmethod
    def construct():
        return CarBuilder() \
            .set_car_brand("BMW") \
            .set_car_model("4.20") \
            .set_number_doors(4) \
            .set_black_box(True) \
            .set_color("Blue") \
            .set_hybrid(True) \
            .set_turbo(True) \
            .set_engine_size(4200) \
            .set_max_speed(380) \
            .get_result()

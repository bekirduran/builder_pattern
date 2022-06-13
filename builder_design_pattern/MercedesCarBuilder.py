
from builder_design_pattern.CarBuilder import CarBuilder


class MercedesCarBuilder:

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return CarBuilder() \
            .set_car_brand("Mercedes") \
            .set_car_model("E250") \
            .set_number_doors(6) \
            .set_sunroof(True) \
            .get_result()

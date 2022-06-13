from builder_design_pattern.AudiCarBuilder import AudiCarBuilder
from builder_design_pattern.BMWCarBuilder import BMWCarBuilder
from builder_design_pattern.MercedesCarBuilder import MercedesCarBuilder

if __name__ == "__main__":
    mercedes = MercedesCarBuilder.construct()
    print(mercedes.produce())

    print("----------------------------")

    audi = AudiCarBuilder.construct()
    print(audi.produce())

    print("----------------------------")

    bmw = BMWCarBuilder.construct()
    print(bmw.produce())




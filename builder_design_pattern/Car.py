class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.door = None
        self.max_speed = None
        self.sunroof = None
        self.engine_size = None
        self.armor = None
        self.hybrid = None
        self.turbo = None
        self.black_box = None

    def produce(self):
        string = ""
        if self.brand is not None:
            string += f"This car name is {self.brand}\n"
        if self.model is not None:
            string += f"model is {self.model}\n"
        if self.color is not None:
            string += f"color : {self.color}\n"
        if self.door is not None:
            string += f"with door: {self.door}\n"
        if self.max_speed is not None:
            string += f"maximum speed : {self.max_speed}\n"
        if self.sunroof is True:
            string += f"it has sunroof \n"
        if self.engine_size is not None:
            string += f"engine size : {self.engine_size}\n"
        if self.armor is True:
            string += f"it has armor\n"
        if self.hybrid is True:
            string += f"it is hybrid car\n"
        if self.turbo is True:
            string += f"it has turbo\n"
        if self.black_box is True:
            string += f"it has black box technology car\n"

        return string

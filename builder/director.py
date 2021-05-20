from builder.house import House, HouseBuilder


class Director:

    def __init__(self) -> None:
        self.builder = HouseBuilder()

    @property
    def builder(self) -> HouseBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: HouseBuilder) -> None:
        self._builder = builder

    def build_minimal_house(self) -> House:
        self.builder.reset()
        self.builder.set_doors(2)
        self.builder.set_rooms(2)
        self.builder.set_walls(4)
        return self.builder.build()

    def build_lux_house(self) -> House:
        self.builder.reset()
        self.builder.set_doors(8)
        self.builder.set_rooms(6)
        self.builder.set_walls(12)
        self.builder.add_garage()
        self.builder.add_garden()
        self.builder.add_swim_pool()
        return self.builder.build()

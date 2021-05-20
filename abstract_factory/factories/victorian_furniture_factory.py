from abstract_factory.furnitures.abstract_furnitures import Chair, Sofa, CoffeeTable
from abstract_factory.factories.furniture_factory import FurnitureFactory
from abstract_factory.furnitures.victorian_furnitures import VictorianChair, VictorianSofa, VictorianCoffeeTable


class VictorianFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

from abstract_factory.furnitures.abstract_furnitures import Chair, Sofa, CoffeeTable
from abstract_factory.factories.furniture_factory import FurnitureFactory
from abstract_factory.furnitures.modern_furnitures import ModernChair, ModernSofa, ModernCoffeeTable


class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

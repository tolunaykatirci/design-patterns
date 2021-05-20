from abstract_factory.factories.furniture_factory import FurnitureFactory
from abstract_factory.factories.modern_furniture_factory import ModernFurnitureFactory
from abstract_factory.factories.victorian_furniture_factory import VictorianFurnitureFactory

'''
Abstract Factory is a creational design pattern that lets you produce families 
of related objects without specifying their concrete classes.

Chair, Sofa, Coffee Table X Modern, Victorian
'''


def client_code(factory: FurnitureFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: FurnitureFactory and abstract furniture Chair, Sofa and Coffee Table.
    This lets you pass any factory or product subclass to the client code without breaking it.
    """
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(f"{chair.chair_feature_1()}")
    print(f"{sofa.sofa_feature_2()}")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the ModernFurnitureFactory:")
    client_code(ModernFurnitureFactory())

    print('\n')

    print("Client: Testing client code with the VictorianFurnitureFactory:")
    client_code(VictorianFurnitureFactory())

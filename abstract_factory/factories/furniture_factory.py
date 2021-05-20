from __future__ import annotations
from abc import ABC, abstractmethod

from abstract_factory.furnitures.abstract_furnitures import Chair, Sofa, CoffeeTable


class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

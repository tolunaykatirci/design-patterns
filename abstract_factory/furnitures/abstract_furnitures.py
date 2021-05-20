from __future__ import annotations
from abc import ABC, abstractmethod


class Chair(ABC):

    @abstractmethod
    def chair_feature_1(self):
        pass

    @abstractmethod
    def chair_feature_2(self):
        pass


class Sofa(ABC):

    @abstractmethod
    def sofa_feature_1(self):
        pass

    @abstractmethod
    def sofa_feature_2(self):
        pass


class CoffeeTable(ABC):

    @abstractmethod
    def coffee_table_feature_1(self):
        pass

    @abstractmethod
    def coffee_table_feature_2(self):
        pass

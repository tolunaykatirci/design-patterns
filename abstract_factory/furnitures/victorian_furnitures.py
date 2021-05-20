from abstract_factory.furnitures.abstract_furnitures import Chair, Sofa, CoffeeTable


class VictorianChair(Chair):

    def chair_feature_1(self):
        return 'VictorianChair - chair_feature_1'

    def chair_feature_2(self):
        return 'VictorianChair - chair_feature_2'


class VictorianSofa(Sofa):

    def sofa_feature_1(self):
        return 'VictorianSofa - sofa_feature_1'

    def sofa_feature_2(self):
        return 'VictorianSofa - sofa_feature_2'


class VictorianCoffeeTable(CoffeeTable):

    def coffee_table_feature_1(self):
        return 'VictorianCoffeeTable - coffee_table_feature_1'

    def coffee_table_feature_2(self):
        return 'VictorianCoffeeTable - coffee_table_feature_2'

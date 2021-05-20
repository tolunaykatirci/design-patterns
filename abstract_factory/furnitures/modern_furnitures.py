from abstract_factory.furnitures.abstract_furnitures import Chair, Sofa, CoffeeTable


class ModernChair(Chair):

    def chair_feature_1(self):
        return 'ModernChair - chair_feature_1'

    def chair_feature_2(self):
        return 'ModernChair - chair_feature_2'


class ModernSofa(Sofa):

    def sofa_feature_1(self):
        return 'ModernSofa - sofa_feature_1'

    def sofa_feature_2(self):
        return 'ModernSofa - sofa_feature_2'


class ModernCoffeeTable(CoffeeTable):

    def coffee_table_feature_1(self):
        return 'ModernCoffeeTable - coffee_table_feature_1'

    def coffee_table_feature_2(self):
        return 'ModernCoffeeTable - coffee_table_feature_2'

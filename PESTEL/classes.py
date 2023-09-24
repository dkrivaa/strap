# This file contains class definitions for PESTEL variables


class PestelVariables:

    category_options = ['politics', 'economics', 'social', 'technology', 'environment', 'legal']
    significance_options = [1, 2, 3, 4]
    trend_options = ['worse', 'neutral', 'better']
    probability_options = [1, 2, 3, 4]

    def __init__(self, category, name, significance, trend, probability):
        self.category = category
        self.name = name
        self.significance = significance
        self.trend = trend
        self.probability = probability

# class Politics(PestelVariables):
#
#     def __init__(self, category, name, significance, trend, probability, geography):
#         super().__init__(category, name, significance, trend, probability)
#         self.geography = geography


# Alejandra Castillo 1440370
class FoodItem:
    # TODO: Define constructor with parameters to initialize instance
    #       attributions (name, fat, carbs, protein)

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}'.format(self.name))
        print('    Fat: {:.2f} g'.format(self.fat))
    print('   Carbohydrates: {:.2f} g'.format(self.carbs))
    print('   Protein: {:.2f} g'.format(self.protein))')


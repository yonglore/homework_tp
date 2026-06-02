from Ingredient import Ingredient


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = list(ingredients)

    def add_ingredient(self, ingredient: Ingredient):
        for elem in self.ingredients:
            if elem == ingredient:
                elem.quantity += ingredient.quantity
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        return False

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффицент должен быть положительным числом")

        res_ingredients = []
        for elem in self.ingredients:
            res_ingredients.append(Ingredient(elem.name, elem.quantity * ratio, elem.unit))

        return Recipe(self.title, res_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        res = f"Рецепт: {self.title} \n Ингредиенты: "
        for elem in self.ingredients:
            res += f"\n • {elem}"
        return res
